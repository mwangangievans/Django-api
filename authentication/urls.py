from authentication import views
from django.urls import path
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("register", views.RegisterApiView, basename="register")
routers.register("login", views.loginApiView, basename="login")


urlpatterns= [] + routers.urls