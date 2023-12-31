from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Index"),
    path('about',views.about,name="about"),
    path('courses',views.courses,name="courses"),
    path('teachers',views.teachers,name="teachers"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('single',views.single,name="single"),
    path('join-us',views.join_us,name="join-us"),
]
