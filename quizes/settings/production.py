from .base import *

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "'smtp.gmail.com'"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.path.join("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.path.join("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

# Redis Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.path.join("REDIS_BACKEND"),
    },
}
DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)
DATABASES["default"].update(db_from_env)
