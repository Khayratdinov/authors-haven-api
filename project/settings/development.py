from .base import *
from .base import env
import importlib


DEBUG = True

SECRET_KEY = env(
    "SECRET_KEY", default="1u_l2m)cay%%)jki^)6%)r$1)qyeh=%uljcs6k^4w0gj_*1ek%"
)
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]


# ================================= DATABASE ================================= #

# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ROOT_DIR / 'db.sqlite3',
#     }
# }


# Check if the debug_toolbar package is installed
if importlib.util.find_spec("debug_toolbar"):
    # Import the debug_toolbar module and add it to the INSTALLED_APPS

    DEBUG_TOOLBAR = True

    import debug_toolbar

    INSTALLED_APPS.append("debug_toolbar")

    # Add debug_toolbar to the MIDDLEWARE
    MIDDLEWARE.insert(
        0,
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    )

    # Set INTERNAL_IPS to allow local access to the debug_toolbar
    INTERNAL_IPS = ["127.0.0.1"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@authors-haven.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
