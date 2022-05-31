from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'', views.home, 'home'),
    url('login/', views.login, 'login'),
    url('register/', views.register, 'register'),
    url('addFace/', views.addFace, 'addFace'),
    url('welcome/<face_id>/', views.welcome, 'welcome')
]
