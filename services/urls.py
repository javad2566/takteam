from django.urls import path
from . import views

app_name="services"


urlpatterns=[
    path("",views.ServicesListView.as_view(),name="list_services"),
    path("detail/<int:id>/",views.service_datail_view,name="detail_services")
    
]