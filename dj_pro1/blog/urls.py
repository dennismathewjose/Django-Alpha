from django.urls import path
from . import views

#creating a path for blog home page
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]
