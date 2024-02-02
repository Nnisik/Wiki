from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="start"),
    path("<str:topic>", views.index, name="index"),
]