from django.contrib import admin
from .models import WorkField,TeamMember,ContactUs
# Register your models here.
@admin.register(TeamMember)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("name","phone","status")
    search_fields = ["name","discription"]
    list_filter = ("status",)
    date_hierarchy = "published_date"


admin.site.register(WorkField)

@admin.register(ContactUs)
class ContatcUsdmin(admin.ModelAdmin):
    list_display = ("title","phone","status")
    search_fields = ["title","discription"]
    list_filter = ("status",)
    date_hierarchy = "published_date"


    