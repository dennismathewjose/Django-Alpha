from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat_view

urlpatterns = [

    path('', views.home, name = 'home'),
    #path('',chatView.videocallview, name ='videocalview')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)