from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about-us', views.about_us, name="about-us"),
    # to store data via form
    path('user', views.user, name="user"),
    path('show-user/<str:name>', views.show_user, name="show_user"),
]
