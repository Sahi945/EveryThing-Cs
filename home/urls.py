from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("search", views.search, name="search"),
    path("loginpage", views.loginpage, name="newlogin"),
    path("signuppage", views.signuppage, name="newlogin"),
    path("login/", views.handleLogin, name="handleLogin"),
    path("signup/", views.handleSignup, name="handleSignup"),
    path("logout", views.handleLogout, name="handleLogout"),
    path("doubts", views.doubts, name="doubts"),
    path('addpost/', views.addpost, name='addpost'),

]
