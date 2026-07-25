FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py import_recipes && \
    (python manage.py createsuperuser --noinput || true) && \
    python manage.py runserver 0.0.0.0:${PORT:-8000}