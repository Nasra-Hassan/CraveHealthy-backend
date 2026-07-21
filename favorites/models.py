from django.conf import settings
from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites"
    )

    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="favorited_by"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"],
                name="unique_user_recipe_favorite"
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.recipe.title}"
