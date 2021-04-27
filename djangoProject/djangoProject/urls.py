"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    # simple html page
    path('about', views.about, name="about"),
    # read and display file
    path('show_one', views.show_one, name="show_one"),
    # show form and process it
    path('form', views.form, name="form"),
    path('process', views.confirm, name="process"),
    # write file
    path('input', views.input_file, name="input_file"),
    path('write', views.write_file, name="write_file"),
    # cookies
    path('last_login_cookie', views.last_login_cookie, name="last_login_cookie"),
    # session
    path('login_session', views.login_session, name="login_session"),
    path('session_saved', views.session_saved, name="session_saved"),
    # send mail
    # will need to set email_id and email_password in env variables for code to run
    path('create_mail', views.create_mail, name="create_mail"),
    path('send_email', views.send_email, name="send_email"),
    # app1 redirect
    path('app1/', include("app1.urls"), name="app1"),
]
