
from django.urls import re_path, include
from . import views 
app_name = "personal"

urlpatterns = [

    re_path('^$', views.index, name='index'),
    re_path('^contact', views.contact, name='contact'),
    re_path("register/", views.register, name="register"),
    re_path("logout", views.logout_request, name="logout"),
    re_path("login", views.login_request, name="login"),
]
