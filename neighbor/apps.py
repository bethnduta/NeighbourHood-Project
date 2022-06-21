from django.apps import AppConfig


class NeighborConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighbor'

    def ready(self):
        import neighbor.signals    
