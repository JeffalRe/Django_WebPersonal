from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    #permite tomar un nombre actual a otro dentro de la interfaz admin Portafolio
    verbose_name='Portafolio'
