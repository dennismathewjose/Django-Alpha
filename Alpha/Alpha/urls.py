"""Alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views
from django.contrib.auth import views as auth_view
from chat import views as chatView
from shareeditor import views as editView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup/',views.signup, name = 'signup'),
    path('login/',auth_view.LoginView.as_view(template_name = 'register/login.html'), name='login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'register/logout.html'),name = 'logout'),
    path('home/', include('home.urls')),
    path('',chatView.videocallview, name ='videocalview'),
    path('chat/<str:room>/<str:created>/',chatView.video, name = 'video'),
    path('editor/',editView.editor,name = 'editor'),

]
