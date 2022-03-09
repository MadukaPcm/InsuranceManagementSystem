from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView, name='homepage_url'),
    path('about/', views.AboutView, name='about_url'),
    path('insurance/', views.InsuranceView, name='insurance_url'),

    path('login/', views.LoginView, name='login_url'),
    path('register/', views.RegisterView, name='register_url'),
    path('forgotpassword/', views.ForgotPasswordView, name='forgotpassword_url'),
    path('logout/', views.SignoutView, name='logout_url'),
]