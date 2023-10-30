from .base import *
from .base import env


ADMINS = [
    (""" Nurpolat """, "khayratdinov.np@gmail.com"),
]

SECRET_KEY = env("SECRET_KEY")

# TODO add domain names of the production servers
CSRF_TRUSTED_ORIGINS = [""]
