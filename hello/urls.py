from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jose", views.jose, name="jose"),
    path("<str:name>", views.greet, name="greet")
]