from django.apps import AppConfig


class GeektideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GeekTide'

def ready(self):
    import GeekTide.signals 