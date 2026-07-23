import requests

from django.core.management.base import BaseCommand
from recipes.models import (
    Recipe,
    Cuisine,
    Flavor,
    Ingredient,
    RecipeIngredient,
)


class Command(BaseCommand):
    help = "Import recipes from TheMealDB API"

    def handle(self, *args, **options):
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s="

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        meals = data.get("meals", [])

        if not meals:
            self.stdout.write(
                self.style.WARNING("No recipes found.")
            )
            return

        imported_count = 0

        for meal in meals:
            title = meal.get("strMeal")

            if not title:
                continue

            cuisine_name = meal.get("strArea") or "Other"
            category_name = meal.get("strCategory") or "Other"

            cuisine, _ = Cuisine.objects.get_or_create(
                name=cuisine_name
            )

            flavor, _ = Flavor.objects.get_or_create(
                name=category_name
            )

            recipe, created = Recipe.objects.update_or_create(
                title=title,
                defaults={
                    "description": (
                        f"{category_name} {cuisine_name} recipe "
                        "imported from TheMealDB."
                    ),
                    "instructions": meal.get(
                        "strInstructions"
                    ) or "No instructions available.",
                    "prep_time": 0,
                    "cook_time": 0,
                    "servings": 1,
                    "calories": None,
                    "protein": None,
                    "carbohydrates": None,
                    "fat": None,
                    "image_url": meal.get(
                        "strMealThumb"
                    ) or "",
                    "cuisine": cuisine,
                    "flavor": flavor,
                }
            )

            if not created:
                RecipeIngredient.objects.filter(
                    recipe=recipe
                ).delete()

            for i in range(1, 21):
                ingredient_name = meal.get(
                    f"strIngredient{i}"
                )
                measurement = meal.get(
                    f"strMeasure{i}"
                )

                if not ingredient_name:
                    continue

                ingredient_name = ingredient_name.strip()

                if not ingredient_name:
                    continue

                ingredient, _ = Ingredient.objects.get_or_create(
                    name=ingredient_name
                )

                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=1,
                    unit=(measurement or "").strip()[:50],
                )

            imported_count += 1

            action = "Imported" if created else "Updated"

            self.stdout.write(
                self.style.SUCCESS(
                    f"{action}: {recipe.title}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSuccessfully imported/updated "
                f"{imported_count} recipes."
            )
        )
