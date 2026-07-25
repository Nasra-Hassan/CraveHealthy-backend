# CraveHealthy API Documentation

Base URL (production): `https://cravehealthy-backend.onrender.com/api/`
Base URL (local): `http://localhost:8000/api/`

## Authentication

CraveHealthy uses JWT authentication (`djangorestframework-simplejwt`). Most endpoints require an `Authorization` header:

```
Authorization: Bearer <access_token>
```

Access tokens are obtained via the **Login** endpoint below and must be included on every request to a protected endpoint. When an access token expires, use the **Refresh Token** endpoint to get a new one.

---

## Users

### Register a new user
`POST /api/users/register/`

**Auth required:** No

**Request body:**
```json
{
  "username": "jane_doe",
  "email": "jane@example.com",
  "password": "strongpassword123",
  "first_name": "Jane",
  "last_name": "Doe"
}
```
`first_name` and `last_name` are optional. `password` must be at least 8 characters.

**Response:** `201 Created`
```json
{
  "username": "jane_doe",
  "email": "jane@example.com",
  "first_name": "Jane",
  "last_name": "Doe"
}
```

---

### Log in
`POST /api/users/login/`

**Auth required:** No

**Request body:**
```json
{
  "username": "jane_doe",
  "password": "strongpassword123"
}
```

**Response:** `200 OK`
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

### Refresh access token
`POST /api/users/token/refresh/`

**Auth required:** No

**Request body:**
```json
{
  "refresh": "<jwt_refresh_token>"
}
```

**Response:** `200 OK`
```json
{
  "access": "<new_jwt_access_token>"
}
```

---

### Get current user
`GET /api/users/me/`

**Auth required:** Yes

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "jane_doe",
  "email": "jane@example.com",
  "first_name": "Jane",
  "last_name": "Doe"
}
```

---

## Recipes

### List all recipes / Create a recipe
`GET /api/recipes/` — list all recipes
`POST /api/recipes/` — create a new recipe

**Auth required:** No (open to all — no permission class set)

**Response (GET):** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Ezme",
    "description": "Vegetarian Turkish recipe imported from TheMealDB.",
    "instructions": "...",
    "prep_time": 15,
    "cook_time": 0,
    "servings": 4,
    "calories": 120,
    "protein": 3.5,
    "carbohydrates": 10.2,
    "fat": 2.1,
    "image_url": "https://...",
    "cuisine": 3,
    "cuisine_name": "Turkish",
    "flavor": 2,
    "flavor_name": "Vegetarian",
    "recipe_ingredients": [
      {
        "id": 10,
        "ingredient": 5,
        "ingredient_name": "Tomato",
        "quantity": 2,
        "unit": "pcs"
      }
    ],
    "created_at": "2026-07-21T12:00:00Z",
    "updated_at": "2026-07-21T12:00:00Z"
  }
]
```

**Request body (POST):**
```json
{
  "title": "New Recipe",
  "description": "A short description",
  "instructions": "Step by step instructions",
  "prep_time": 10,
  "cook_time": 20,
  "servings": 2,
  "calories": 350,
  "protein": 20.5,
  "carbohydrates": 30.0,
  "fat": 12.0,
  "image_url": "https://example.com/image.jpg",
  "cuisine": 1,
  "flavor": 2
}
```

---

### Retrieve, update, or delete a recipe
`GET /api/recipes/<id>/`
`PUT` / `PATCH /api/recipes/<id>/`
`DELETE /api/recipes/<id>/`

**Auth required:** No (open to all — no permission class set)

Returns/accepts the same shape as above, scoped to a single recipe. `DELETE` returns `204 No Content`.

---

## Ingredients

### List all ingredients / Create an ingredient
`GET /api/ingredients/`
`POST /api/ingredients/`

**Auth required:** No

**Response (GET):** `200 OK`
```json
[
  { "id": 1, "name": "Tomato" },
  { "id": 2, "name": "Garlic" }
]
```

**Request body (POST):**
```json
{ "name": "Basil" }
```

---

### Retrieve, update, or delete an ingredient
`GET /api/ingredients/<id>/`
`PUT` / `PATCH /api/ingredients/<id>/`
`DELETE /api/ingredients/<id>/`

**Auth required:** No

---

## Favorites

### List current user's favorites / Add a favorite
`GET /api/favorites/` — list the logged-in user's favorited recipes
`POST /api/favorites/` — favorite a recipe

**Auth required:** Yes

**Response (GET):** `200 OK`
```json
[
  {
    "id": 4,
    "user": 1,
    "recipe": 7,
    "recipe_title": "Kabse",
    "recipe_details": { "...full recipe object..." },
    "created_at": "2026-07-25T10:00:00Z"
  }
]
```

**Request body (POST):**
```json
{ "recipe": 7 }
```
`user` is set automatically from the authenticated request — do not send it.

---

### Retrieve or remove a favorite
`GET /api/favorites/<id>/`
`DELETE /api/favorites/<id>/`

**Auth required:** Yes

Only the owning user's favorites are accessible — requests for another user's favorite `id` return `404 Not Found`. `DELETE` returns `204 No Content`.

---

## Admin panel

Django's built-in admin is available at:
```
/admin/
```
Requires a superuser account.

## Notes

- All endpoints return standard DRF error shapes on validation failure, e.g. `{"field_name": ["This field is required."]}`, with status `400 Bad Request`.
- Unauthenticated requests to protected endpoints return `401 Unauthorized`.
- The free-tier deployment spins down after inactivity; the first request after idling may take up to ~50 seconds to respond.