from django.contrib import admin
from django.urls import path
from myBlogs import views

urlpatterns = [
   path('' , views.index , name='myBlogs'),
   path('' , views.home , name='myBlogs'),
]