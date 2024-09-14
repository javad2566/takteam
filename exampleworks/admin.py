from django.contrib import admin
from .models import Work,Category
# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title","published_date","status")
    search_fields = ["title","discription"]
    list_filter = ("status",)
    date_hierarchy = "published_date"


admin.site.register(Category)