import os
from flask_caching.backends.filesystemcache import FileSystemCache

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Provided by Render

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY must be set for security. Define it as an environment variable.")

# Optional: Enable BigQuery
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# Redis URL from environment variable, example: redis://:password@red-xxxx:6379/1
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/1")

## REDIS SERVICE
# # RedisCache config for query results
# RESULTS_BACKEND = {
#     "CACHE_TYPE": "RedisCache",
#     "CACHE_DEFAULT_TIMEOUT": 300,
#     "CACHE_KEY_PREFIX": "superset_results_",
#     "CACHE_REDIS_URL": REDIS_URL,
# }

# # General caching config (e.g., for dashboards, charts)
# CACHE_CONFIG = {
#     "CACHE_TYPE": "RedisCache",
#     "CACHE_DEFAULT_TIMEOUT": 300,
#     "CACHE_KEY_PREFIX": "superset_",
#     "CACHE_REDIS_URL": REDIS_URL,
# }
#
# # Celery (async tasks) config
# class CeleryConfig:
#     broker_url = REDIS_URL  # Typically Redis DB 0
#     result_backend = REDIS_URL
#     worker_prefetch_multiplier = 1
#     task_acks_late = False

# CELERY_CONFIG = CeleryConfig

# REDIS LOCAL

RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

CACHE_CONFIG = {
    "CACHE_TYPE": "FileSystemCache",
    "CACHE_DIR": "/app/superset_home/cache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}


# This is used by explore view
DATA_CACHE_CONFIG = CACHE_CONFIG

