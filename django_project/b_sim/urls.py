from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('help/', views.about, name='blog-help'),
]