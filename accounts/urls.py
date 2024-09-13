from django.urls import path 
from . import views

app_name = "accounts"

urlpatterns =[
  path("logout/",views.logout_view,name="logout"),

  path("login/",views.LoginView.as_view(),name="login"),

  path("register/",views.RegisterView.as_view(),name="register"),
  # path("register/code/",views.CodeConfirmView.as_view(),name="code")
  ]