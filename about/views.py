from django.shortcuts import render,redirect
from .models import TeamMember,ContactUs
# Create your views here.
from django.utils import timezone

from django.contrib import messages

def about_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        if title and discription and request.user.email:
            ContactUs.objects.create(title=title,disctption=discription,phone=request.user.phone,email=request.user.email)
            messages.success(request,"تیکت شما ارسال شد . ")
            return redirect("/")
        else:
            messages.error(request,"عنوان و توضیحات و ایمیل اجباری است ")
    time_now = timezone.now()
    teammembers = TeamMember.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
    return render(request,"about/about.html",{"team_members":teammembers})