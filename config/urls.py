"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/recipes/', include('recipes.urls')),
    path('api/ingredients/', include('ingredients.urls')),
    path('api/favorites/', include('favorites.urls')),
    path('api/users/', include('users.urls')),
]