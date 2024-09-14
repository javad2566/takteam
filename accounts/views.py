from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate
from accounts.models import User,OTP
from django.utils.crypto import get_random_string
from random import randint
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"خروج از حساب با موفقیت انجام شد ")
        return redirect("/")

    messages.error(request,"خروج از حساب انجام نشد ")
    return redirect("/")


class LoginView(TemplateView):
    template_name = "accounts/login.html"
    
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"ورود به حساب با موفقیت انجام شد . ")
            return redirect("/accounts/profile")
        messages.error(request,"ورود به حساب انجام نشد ")
        return render(request,"accounts/login.html")
    
    
    
    
class RegisterView(TemplateView):
    template_name = "accounts/register.html"
    
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        for user in User.objects.all():
            if int(user.phone) == int(username):
                messages.error(request,"کاربر با این شماره در سایت وجود دارد.")
                return render(request,"accounts/register.html")
        if password1 != password2:
            messages.error(request,"رمز عبور شما با یکدیگر مطابقت ندارد .")
            return render(request,"accounts/register.html")

        else:
            code = randint(1000,10000)
            token = get_random_string(length=150)
            OTP.objects.create(phone=username,code=code,token=token,password=password1)
            print(code)
            messages.success(request,f"کد به ارسال شد {username} ")
            return redirect(f"/accounts/register/code/?phone={token}")


class CodeConfirmRegisterView(TemplateView):
    template_name = "accounts/code_confirm_register.html"


    def post(self,request):
        token = request.GET.get("phone")
        code = request.POST.get("code")
        print(f"code post {code}")
        otp_user = OTP.objects.get(token=token)
        print(f"code otp {otp_user.code}")
        if int(code) == int(otp_user.code) :
            new_user = User.objects.create(phone=otp_user.phone)
            new_user.set_password(otp_user.password)
            new_user.save()
            otp_user.delete()
            messages.success(request,"کاربر با موفقیت ایجاد شد ")
            return redirect("/")
        else:
            messages.error(request," کد تایید نامتعبر است لحظاتی بعد مجددا تلاش کنید")
            otp_user.delete()
            return redirect("/accounts/register")
        
        
        
class ProfileView(TemplateView):
    template_name = "accounts/profile_user.html"
    
    def post(self,request):
        request.user.email = request.POST.get("email")
        request.user.fullname = request.POST.get("name")
        request.user.address = request.POST.get("address")
        request.user.discription = request.POST.get("discription")
        
        request.user.save()
        messages.success(request,"پروفایل شما تغییر کرد.")
        return redirect("/")
