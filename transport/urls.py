from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update-location/', views.update_location, name='update_location'),
    path('update-passenger/', views.update_passenger, name='update_passenger'),
    path('driver-tracking/', views.driver_tracking, name='driver_tracking'),
    path('auto-save-location/', views.auto_save_location, name='auto_save_location'),

]