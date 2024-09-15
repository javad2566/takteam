from django.urls import path
from . import views
app_name = "exampleworks"

urlpatterns =[
    path("list/",views.ListExampleWorksView.as_view(),name="listworks"),
    path("detail/<int:id>/",views.SingleExampleWorkView.as_view(),name="detailwork"),
]