import os
from flask_caching.backends.redis import RedisCache

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Provided by Render

SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

# Optional: Enable BigQuery
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

REDIS_URL = os.getenv("REDIS_URL")  # e.g. redis://:password@red-xxxx:6379/1

RESULTS_BACKEND = RedisCache.from_url(REDIS_URL)

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": REDIS_URL,
}
DATA_CACHE_CONFIG = CACHE_CONFIG

class CeleryConfig:
    broker_url = os.getenv("REDIS_URL")  # Same or use /0
    result_backend = os.getenv("REDIS_URL")
    worker_prefetch_multiplier = 1
    task_acks_late = False

CELERY_CONFIG = CeleryConfig