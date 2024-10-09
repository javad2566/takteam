from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate
from accounts.models import User,OTP
from django.utils.crypto import get_random_string
from random import randint
import ghasedakpack
from home.captcha import CaptchaForm

sms = ghasedakpack.Ghasedak("5a36e1045f08fd777bd67da30f8702863765d5f8ceb420324c7da377aafd5707")
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
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"ورود به حساب با موفقیت انجام شد . ")
                return redirect("/accounts/profile")
            else:
                messages.error(request,"ورود به حساب انجام نشد ")
                return redirect("/accounts/login")
        else:
            messages.error(request,"کد کپچا درست نیست ")
            return redirect("/accounts/login")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = CaptchaForm()
        return context
    
    
    
    
class RegisterView(TemplateView):
    template_name = "accounts/register.html"
    
    def post(self,request):
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            for user in User.objects.all():
                if int(user.phone) == int(username):
                    messages.error(request,"کاربر با این شماره در سایت وجود دارد.")
                    return redirect("/accounts/register/")
            if password1 != password2:
                messages.error(request,"رمز عبور شما با یکدیگر مطابقت ندارد .")
                return redirect("/accounts/register/")

            else:
                code = randint(1000,10000)
                token = get_random_string(length=150)
                print(username,code)
                sms.verification({'receptor' : f'{username}','type':'1',"template":"randcode","param1":f"{code}"})
                OTP.objects.create(phone=username,code=code,token=token,password=password1)
                print(code)
            
                messages.success(request,f"کد به ارسال شد {username} ")
                return redirect(f"/accounts/register/code/?phone={token}")
        else:
            messages.error(request,"کد کپچا درست نیست ")
            return redirect("/accounts/register/")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = CaptchaForm()
        return context


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
    template_name ="accounts/profile_user.html"
    
    def post(self,request):
        request.user.email = request.POST.get("email")
        request.user.fullname = request.POST.get("name")
        request.user.address = request.POST.get("address")
        request.user.discription = request.POST.get("discription")
        
        if len(request.FILES) != 0:
            request.user.image = request.FILES["image"]
       
        request.user.save()
        messages.success(request,"پروفایل شما تغییر کرد.")
        return redirect("/")


class ForgetPasswordView(TemplateView):
    template_name = "accounts/forgot_password.html"

    def post(self,request):
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            code = randint(1000,10000)
            token = get_random_string(length=150)
            print(username,code)
            sms.verification({'receptor' : f'{username}','type':'1',"template":"randcode","param1":f"{code}"})
            print(code)
            OTP.objects.create(phone=username,code=code,token=token,password=123)
        else:
            messages.error(request,"کد کپچا درست نیست ")
            return redirect("/accounts/forget-password/")

        messages.success(request,f"کد تایید به شماره تماس {username}ارسال شد ")
        return redirect(f"/accounts/confirm-code/?token={token}")
    

    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["form"] = CaptchaForm()
        return context

class ForgetPasswordConfirmCodeView(TemplateView):
    template_name = "accounts/forget-password-code.html"



    def post(self,request):
        token =request.GET.get("token")
        code = request.POST.get("code")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        otp_user  = OTP.objects.get(token=token)
        user = User.objects.get(phone=otp_user.phone)
        print(user)
        if otp_user.code == int(code):
            if password1 == password2:
                
                user.set_password(password1)
                user.save()
                messages.success(request,"رمز عبور تغییر کرد ")
                return redirect("/")
            else:
                otp_user.delete()
                messages.error(request,"رمز عبور مطابق نیست ")
                return redirect("/")
        else:
            otp_user.delete()
            messages.error(request,"کد تایید درست نیست ")
            return redirect("/")

