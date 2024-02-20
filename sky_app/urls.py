from django.urls import path

from . import views


urlpatterns = [

path('', views.sky, name='sky'),
path('aboutus/', views.aboutus, name='aboutus'),


]

