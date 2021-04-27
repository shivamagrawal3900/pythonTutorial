from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us', views.about_us, name="about-us"),
]
