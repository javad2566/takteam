from django.urls import path
from . import views
app_name = "exampleworks"

urlpatterns =[
    path("list/",views.ListExampleWorksView,name="list"),
    path("detail/<int:id>/",views.work_datail_view,name="detail"),
]