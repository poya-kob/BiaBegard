from django.apps import AppConfig


class ApiBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_blog'

    def ready(self):
        import api_blog.signal
