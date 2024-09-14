from django.urls import path
from . import views
app_name = "exampleworks"

urlpatterns =[
    path("list/",views.ListExampleWorksView.as_view(),name="listworks")
]