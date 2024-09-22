from django.urls import path
from .import views

app_name="courses"

urlpatterns = [
    path("list/",views.course_list_view,name="list_courses"),
    path("detail/<int:id>/",views.course_datail_view,name="detail_courses")
]