from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Flavor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()

    prep_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes"
    )
    cook_time = models.PositiveIntegerField(
        help_text="Cooking time in minutes"
    )

    servings = models.PositiveIntegerField(default=1)

    calories = models.PositiveIntegerField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fat = models.FloatField()

    image_url = models.URLField(blank=True)

    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes"
    )

    flavor = models.ForeignKey(
        Flavor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )

    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient.name}"
