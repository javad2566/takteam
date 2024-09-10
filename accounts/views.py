from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
        return redirect("/")

    messages.error(request,"not logout ")
    return redirect("/")