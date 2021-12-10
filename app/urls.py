from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('Teacher', views.Teacher, name='Teacher'),
    path('Courses', views.Courses, name='Courses'),
    path('Pricing', views.Pricing, name='Pricing'),
    path('Blog', views.Blog, name='Blog'),
    path('Contact', views.Contact, name='Contact')
]