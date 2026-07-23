from rest_framework import serializers
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    recipe_title = serializers.CharField(
        source="recipe.title",
        read_only=True
    )

    class Meta:
        model = Favorite
        fields = [
            "id",
            "user",
            "recipe",
            "recipe_title",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "recipe_title",
            "created_at",
        ]
