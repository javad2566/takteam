from django.shortcuts import render,redirect
from .models import TeamMember,ContactUs,Subscribe
# Create your views here.
from django.utils import timezone
from django.views import View

from django.contrib import messages
from home.captcha import CaptchaForm
def about_view(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            title = request.POST.get("title")
            email = request.POST.get("email")
            discription = request.POST.get("discription")
            print(title,discription,email)
            if title and discription and email:
                ContactUs.objects.create(title=title,disctption=discription,email=email)
                messages.success(request,"تیکت شما ارسال شد . ")
                return redirect("/")
            else:
                messages.error(request,"عنوان و توضیحات و ایمیل اجباری است ")
                return redirect("/about")
        else:
            messages.error(request,"کد کپچا درست نیست ")
            return redirect("/about")
        
    
    form =CaptchaForm()

    time_now = timezone.now()
    teammembers = TeamMember.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("created_date")
    return render(request,"about/about.html",{"team_members":teammembers ,"form":form})




