from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project.apps.profiles"
    verbose_name = _("Profiles")

    def ready(self):
        from project.apps.profiles import signals
