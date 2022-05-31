from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'', views.home),
    url('login/', views.login),
    url('register/', views.register),
    url('addFace/', views.addFace),
    url('welcome/<face_id>/', views.welcome)
]
