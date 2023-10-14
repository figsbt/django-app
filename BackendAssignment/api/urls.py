from django.urls import path
from . import views

urlpatterns = [
    path("api-app-info", views.info, name="info"),
]