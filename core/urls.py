from django.urls import path
from . import views

urlpatterns = [
    path("", views.hellotime, now="hellotime"),
    path("screenprint", views.screenprint, name="screenprint")
]