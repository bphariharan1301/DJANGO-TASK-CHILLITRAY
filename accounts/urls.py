
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.register, name='register'),
    path('verify', views.verify, name='verify'),
    path('logout', views.logout, name='logout'),
]
