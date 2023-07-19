from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),     #base url : this blog url will handle home and about route

    path('about/', views.about, name='blog-about'),
]