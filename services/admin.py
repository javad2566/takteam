from django.contrib import admin
from .models import Service,OrderWork
# Register your models here.
@admin.register(Service)
class SerivecAdmin(admin.ModelAdmin):
    list_display = ("title","published_date","status")
    search_fields = ["title","discription"]
    list_filter = ("status","counted_view")
    date_hierarchy = "published_date"


@admin.register(OrderWork)
class OrderWorkAdmin(admin.ModelAdmin):
    list_display = ("title","created_date","work","user")
    search_fields = ["title","discription"]
    date_hierarchy = "created_date"