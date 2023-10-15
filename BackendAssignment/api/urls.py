from django.urls import path
from . import views


urlpatterns = [
    
    path("api-app-info", views.info, name="api-app-info"),
    
    path("create-user", views.create_user, name="create-user"),
    path("login-user", views.login_user, name="login-user"),

    path("create-post", views.create_post, name="create-post")

]