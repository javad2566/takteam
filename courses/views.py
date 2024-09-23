from django.shortcuts import render,get_object_or_404,redirect
from .models import Course,Category
# Create your views here.
from django.contrib import messages
from django.utils import timezone

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


    courses = Paginator(courses,2)
    try :
        page_number = request.GET.get("page")
        courses = courses.get_page(page_number)
    
    except PageNotAnInteger:
        courses = courses.get_page(1)
    except EmptyPage :
        courses = courses.get_page(1)
    return render(request,"courses/list.html",{"courses":courses,"categorys":categorys,"username":username,"cat_name":cat_name})


def course_datail_view(request,id):
    time_now = timezone.now()
    courses = Course.objects.exclude(published_date__gt=time_now).filter(status=True)
    course = get_object_or_404(courses,id=id)
    course.counted_view +=1 
    course.save()

    return render(request,"courses/detail.html",{"course":course})