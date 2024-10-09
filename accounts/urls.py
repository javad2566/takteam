from django.urls import path 
from . import views

app_name = "accounts"

urlpatterns =[
  path("logout/",views.logout_view,name="logout"),
  path("profile/",views.ProfileView.as_view(),name="profile"),
  path("login/",views.LoginView.as_view(),name="login"),
  path("register/",views.RegisterView.as_view(),name="register"),
  path("forget-password/",views.ForgetPasswordView.as_view(),name="forget-password"),
  path("confirm-code/",views.ForgetPasswordConfirmCodeView.as_view(),name="forget-password-confirm-code"),
  path("register/code/",views.CodeConfirmRegisterView.as_view(),name="code")
  ]