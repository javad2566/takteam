from django.shortcuts import render,get_object_or_404,redirect
from .models import Course,Category,Comment
# Create your views here.
from django.contrib import messages
from django.utils import timezone
from home.captcha import CaptchaForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def course_list_view(request,**kwargs):
    time_now = timezone.now()
    categorys = Category.objects.all()
    courses = Course.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
    cat_name = ""
    username = ""

    if kwargs.get("cat_name") != None:
        cat_name = kwargs.get("cat_name")
        courses = courses.filter(category__name=kwargs.get("cat_name"))


    if kwargs.get("username") != None:
        username = kwargs.get("username")
        courses = courses.filter(teacher__contains=kwargs.get("username"))


    search = request.GET.get("search")
    if search:
        courses =  Course.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date").filter(title__contains=search)
    courses = Paginator(courses,2)
    try :
        page_number = request.GET.get("page")
        courses = courses.get_page(page_number)
    
    except PageNotAnInteger:
        courses = courses.get_page(1)
    except EmptyPage :
        courses = courses.get_page(1)
    return render(request,"courses/list.html",{"courses":courses,"categorys":categorys,"username":username,"cat_name":cat_name ,"search":search})


def course_datail_view(request,id):
    time_now = timezone.now()
    courses = Course.objects.exclude(published_date__gt=time_now).filter(status=True)
    course = get_object_or_404(courses,id=id)
    comments = Comment.objects.filter(course=course,allow=True)
    course.counted_view +=1 
    course.save()
    post_next = ""
    post_prev = ""
    for item in courses:
        if item.id > course.id and Course.objects.filter(id=item.id,status=True):
            post_next = get_object_or_404(Course,id=item.id)
            break
        elif item.id < course.id and Course.objects.filter(id=item.id,status=True):
            post_prev = get_object_or_404(Course,id=item.id)

    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            if request.user.is_authenticated:
                    Comment.objects.create(course=course,name=name,email=email,message=message)
                    messages.success(request,"نظر شما ثبت شد و بعد از بررسی نمایش داده می شود ")
                    return redirect(f"/courses/detail/{course.id}")
            else:
                    Comment.objects.create(course=course,name=name,email=email,message=message)
                    messages.success(request,"نظر شما ثبت شد و بعد از بررسی نمایش داده می شود ")
                    return redirect(f"/courses/detail/{course.id}")
        else:
            messages.error(request,"کد کپتچا درست نیست")
            return redirect(f"/courses/detail/{course.id}")

    else:
        form =CaptchaForm()    


    return render(request,"courses/detail.html",{"course":course , "post_prev":post_prev,"post_next":post_next ,"comments":comments ,"form":form})