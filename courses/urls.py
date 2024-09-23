from django.urls import path
from .import views

app_name="courses"

urlpatterns = [
    path("list/",views.course_list_view,name="list_courses"),
    path("detail/<int:id>/",views.course_datail_view,name="detail_courses"),
    path("category/<str:cat_name>/",views.course_list_view,name="category_courses"),
    path("author/<str:username>/",views.course_list_view,name="author_courses"),
]