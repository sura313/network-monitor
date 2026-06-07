from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_device, name='add_device'),
    path('check/<int:pk>/', views.check_device, name='check_device'),
    path('check-all/', views.check_all, name='check_all'),
    path('device/<int:pk>/', views.device_detail, name='device_detail'),
    path('delete/<int:pk>/', views.delete_device, name='delete_device'),
]