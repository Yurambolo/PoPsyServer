from django.urls import path
from apis.views import apiViews as views

urlpatterns = [
    path('getContent/', views.getContent),
    path('register/', views.register),
    path('signIn/', views.singIn),
    path('getUser/', views.getUser),
    path('sign_s3/', views.sign_s3),
]