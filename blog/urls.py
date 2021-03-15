
from blog.views import addblog
from django.urls import path, include
from blog import views

urlpatterns = [

    path('addblog', views.addblog, name='addblog'),
    path('postComment', views.postComment, name='postComment'),
    path('', views.blogHome, name='home'),

    path('<str:slug>', views.blogPost, name='blogpost'),

]
