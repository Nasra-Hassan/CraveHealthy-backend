from rest_framework import serializers
from .models import Favorite
from recipes.serializers import RecipeSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    recipe_details = RecipeSerializer(
        source="recipe",
        read_only=True
    )

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
            "recipe_details",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "recipe_title",
            "recipe_details",
            "created_at",
        ]
