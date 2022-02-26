from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Home', views.Home, name='Home'),
    path('Physics', views.Physics, name='Physics'),
    path('Mathematics_1', views.Mathematics_1, name='Mathematics_1'),
    path('BME', views.BME, name='BME'),
    path('ES', views.ES, name='ES'),
    path('Other', views.Other, name='Other'),
    
]