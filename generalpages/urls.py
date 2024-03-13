from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home"),
    path("menu/", views.menu_page, name="menu"),
]
