from django.apps import AppConfig

from user.constants import DEFAULT_USER


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        # pass
        from django.contrib.auth import get_user_model
        User = get_user_model()
        default_user_exists = User.objects.filter(username=DEFAULT_USER).exists()
        if not default_user_exists:
            User.objects.create(
                username="default",
            )
