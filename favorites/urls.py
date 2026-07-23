from django.urls import path
from .views import FavoriteListCreateView, FavoriteDetailView

urlpatterns = [
    path('', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('<int:pk>/', FavoriteDetailView.as_view(), name='favorite-detail'),
]
