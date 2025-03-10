OPEN_ROUTES = [
    "http://localhost:8000/",
    "http://localhost:8000/docs",
    "http://localhost:8000/openapi.json",
    "http://localhost:8000/login",
]

import os

RABBIT_URL = (
    "amqp://"
    + os.getenv("RABBITMQ_USER")
    + ":"
    + os.getenv("RABBITMQ_PASSWORD")
    + "@"
    + os.getenv("RABBITMQ_HOST")
    + ":"
    + os.getenv("RABBITMQ_PORT")
)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = int(os.getenv("DB_PORT"))

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")

# Shopify Credentials
API_KEY = os.getenv("API_KEY", None)
API_SECRET_KEY = os.getenv("API_SECRET_KEY", None)
ADMIN_API_ACCESS_TOKEN = os.getenv("ADMIN_API_ACCESS_TOKEN", None)


MYE_INVENTORY_AND_MAPPING_SERVICE_URL = os.environ.get("MIAMS_URL")
MYE_ORDER_SERVICE_URL = os.environ.get("MYE_ORDER_SERVICE_URL")
INTEGRATION_SERVICE = os.environ.get("INTEGRATION_SERVICE")
