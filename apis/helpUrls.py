from django.urls import path
from apis.views import apiViews as views

urlpatterns = [
    path('getMusicPlayLists/', views.getMusicPlayLists),
    path('register/', views.register),
    path('signIn/', views.singIn)
]