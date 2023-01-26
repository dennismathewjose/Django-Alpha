from django.urls import path
from . import views

urlpatterns = [

    path('chat/<str:room>/<str:created>/',views.videocallview, name = 'videocallview')
]