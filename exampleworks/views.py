from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from .models import Work,Category,Comment
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from courses.models import Category
from django.utils import timezone
from home.captcha import CaptchaForm

def ListExampleWorksView(request):
        time_now = timezone.now()
        works = Work.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
        search = request.GET.get("search")
        time_now = timezone.now()

        if search:
            works =  Work.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date").filter(title__contains=search)
        return render(request,"exampleworks/list.html",{"all_works":works ,"search":search})



def work_datail_view(request,id):
    time_now = timezone.now()
    categorys = Category.objects.all()
    form = CaptchaForm()
    works = Work.objects.exclude(published_date__gt=time_now).filter(status=True)
    work = get_object_or_404(works,id=id)
    work.counted_view +=1
    work.save()
    comments = Comment.objects.filter(work=work,allow=True)
    post_next = ""
    post_prev = ""
    for item in works:
        if item.id > work.id and Work.objects.filter(id=item.id,status=True):
            post_next = get_object_or_404(Work,id=item.id)
            break
        elif item.id < work.id and Work.objects.filter(id=item.id,status=True):
            post_prev = get_object_or_404(Work,id=item.id)

    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            if request.user.is_authenticated:
                Comment.objects.create(work=work,name=name,email=email,message=message)
                messages.success(request,"نظر شما ثبت شد و بعد از بررسی نمایش داده می شود ")
                return redirect(f"/example-works/detail/{work.id}")
            else:
                Comment.objects.create(work=work,name=name,email=email,message=message)
                messages.success(request,"نظر شما ثبت شد و بعد از بررسی نمایش داده می شود ")
                return redirect(f"/example-works/detail/{work.id}")
        else:
            messages.error(request,"کد کپچا درست نیست ")
            return redirect(f"/example-works/detail/{work.id}")

    return render(request,"exampleworks/detail.html",{"work":work,"categorys":categorys , "post_prev":post_prev,"post_next":post_next ,"comments":comments,"form":form})