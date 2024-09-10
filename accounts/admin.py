from django import forms
from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserRegister(admin.ModelAdmin):
    list_display = ("phone", "fullname", "is_admin")