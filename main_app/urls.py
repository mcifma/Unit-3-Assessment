from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.createWacky, name='create_wacky'),
    path('', views.deleteWacky, name='delete_wacky'),
]