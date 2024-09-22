from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
# Create your views here.
from django.contrib import messages
from django.utils import timezone



def course_list_view(request):
    time_now = timezone.now()
    courses = Course.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
    return render(request,"courses/list.html",{"courses":courses})


def course_datail_view(request,id):
    time_now = timezone.now()
    courses = Course.objects.exclude(published_date__gt=time_now).filter(status=True)
    course = get_object_or_404(courses,id=id)

    return render(request,"courses/detail.html",{"course":course})