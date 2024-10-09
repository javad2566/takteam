from django.contrib import admin

# Register your models here.
from .models import Course,Category,Comment
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","published_date","status")
    search_fields = ["title","discription"]
    list_filter = ("status","category")
    date_hierarchy = "published_date"


admin.site.register(Category)
admin.site.register(Comment)