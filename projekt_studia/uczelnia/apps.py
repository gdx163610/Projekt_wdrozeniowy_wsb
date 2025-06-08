from django.apps import AppConfig


class UczelniaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uczelnia'

    def ready(self):
        import uczelnia.signals  # Rejestracja sygnałów
