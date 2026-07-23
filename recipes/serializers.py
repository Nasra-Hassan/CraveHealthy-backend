from rest_framework import serializers
from .models import (
    Cuisine,
    Flavor,
    Ingredient,
    Recipe,
    RecipeIngredient,
)


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = [
            "id",
            "name",
        ]
        read_only_fields = ["id"]


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = [
            "id",
            "name",
        ]
        read_only_fields = ["id"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            "id",
            "name",
        ]
        read_only_fields = ["id"]


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.CharField(
        source="ingredient.name",
        read_only=True
    )

    class Meta:
        model = RecipeIngredient
        fields = [
            "id",
            "ingredient",
            "ingredient_name",
            "quantity",
            "unit",
        ]
        read_only_fields = ["id", "ingredient_name"]


class RecipeSerializer(serializers.ModelSerializer):
    cuisine_name = serializers.CharField(
        source="cuisine.name",
        read_only=True
    )

    flavor_name = serializers.CharField(
        source="flavor.name",
        read_only=True
    )

    recipe_ingredients = RecipeIngredientSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "instructions",
            "prep_time",
            "cook_time",
            "servings",
            "calories",
            "protein",
            "carbohydrates",
            "fat",
            "image_url",
            "cuisine",
            "cuisine_name",
            "flavor",
            "flavor_name",
            "recipe_ingredients",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "cuisine_name",
            "flavor_name",
            "recipe_ingredients",
            "created_at",
            "updated_at",
        ]
