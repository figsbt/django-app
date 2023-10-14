"""
    URL configuration for BackendAssignment project.
    The `urlpatterns` list routes URLs to views.
"""

from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),
]
