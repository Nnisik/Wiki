from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="start_page"),
    path("<str:topic>", views.index, name="info_page"),
]