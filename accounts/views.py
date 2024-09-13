from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate
from accounts.models import User

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
            return redirect("/")
        messages.error(request,"ورود به حساب انجام نشد ")
        return render(request,"accounts/login.html")
    
    
    
    
class RegisterView(TemplateView):
    template_name = "accounts/register.html"
    
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            messages.error(request,"رمز عبور شما با یکدیگر مطابقت ندارد .")
            return render(request,"accounts/register.html")

        else:
            new_user = User.objects.create(phone=username)
            print(password1)
            new_user.set_password(password1)
            new_user.save()
            messages.success(request,"کاربر ایجاد شد.")
            return redirect("/")



