from django.apps import AppConfig


class WwwConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WWW'
    verbose_name = "Настройки сайта"
    verbose_name_plural = "Настройка сайта"
