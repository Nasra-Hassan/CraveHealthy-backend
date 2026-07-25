# CraveHealthy 🥗

CraveHealthy is a full-stack recipe app that helps people eat healthy without food feeling boring. Users can browse a curated library of healthy, delicious recipes, view detailed nutrition and preparation info, and save their favorites — all recipes are curated by the admin rather than open community submissions.

## Live demo

- **App:** https://cravehealthy-frontend.onrender.com
- **API:** https://cravehealthy-backend.onrender.com
- **Admin panel:** https://cravehealthy-backend.onrender.com/admin/

> Note: both services run on Render's free tier and spin down after periods of inactivity. The first request after idling may take up to ~50 seconds to respond.

## Repositories

This project is split across two repositories:

- **Frontend:** [CraveHealthy-frontend](https://github.com/Nasra-Hassan/CraveHealthy-frontend) — React + Vite
- **Backend:** [CraveHealthy-backend](https://github.com/Nasra-Hassan/CraveHealthy-backend) — Django REST Framework

## Features

- Browse a curated library of healthy recipes with full nutrition info (calories, protein, carbs, fat)
- Filter recipes by cuisine and flavor/dietary category
- View detailed ingredient lists and step-by-step instructions per recipe
- User registration and JWT-based authentication
- Save and manage favorite recipes per user
- Admin-curated content — recipes are sourced from TheMealDB and managed by the admin, not open to public submissions

## Tech stack

**Frontend**
- React (Vite)
- React Router
- Axios
- Bootstrap

**Backend**
- Django 6 + Django REST Framework
- PostgreSQL
- JWT authentication (`djangorestframework-simplejwt`)
- `django-cors-headers`

**Infrastructure**
- Docker (both frontend and backend containerized)
- Nginx (serving the production frontend build)
- Render (hosting: Web Services + managed PostgreSQL)
- GitHub Actions (CI/CD)

## Database schema

See [`db_diagram.png`](./cravehealthy_db_erd.png) for the full entity-relationship diagram. Core entities: `User`, `Recipe`, `Cuisine`, `Flavor`, `Ingredient`, `RecipeIngredient`, `Favorite`.

## API documentation

Full endpoint documentation, including request/response examples and authentication details, is in [`API.md`](./API.md).

## Running locally

### Prerequisites
- Docker and Docker Compose
- Node.js 20+ (if running the frontend outside Docker)
- Python 3.12+ (if running the backend outside Docker)

### Backend

```bash
git clone https://github.com/Nasra-Hassan/CraveHealthy-backend.git
cd CraveHealthy-backend
```

Create a `.env` file in the project root with:
```
DB_NAME=cravehealthy_db
DB_USER=cravehealthy_user
DB_PASSWORD=your_local_password
DB_HOST=db
DB_PORT=5432
DEBUG=True
```

Run with Docker:
```bash
docker compose up --build
```

The API will be available at `http://localhost:8000/`.

### Frontend

```bash
git clone https://github.com/Nasra-Hassan/CraveHealthy-frontend.git
cd CraveHealthy-frontend
```

Create a `.env` file in the project root with:
```
VITE_API_URL=http://localhost:8000
```

Run with Docker:
```bash
docker compose up --build
```

The app will be available at `http://localhost:3000/`.

## Deployment

Both services are deployed on [Render](https://render.com):
- The backend runs as a Dockerized Web Service connected to a managed PostgreSQL instance.
- The frontend runs as a Dockerized Web Service, built with `VITE_API_URL` pointing at the deployed backend.
- Migrations and the initial superuser are created automatically on container startup.

## Author

Nasra Hassan