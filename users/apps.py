from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"


    # Aqui toca configurar para que se asigne la funcion
    # sobreecribimos metodo ready
    def ready(self):
        import users.signals # con este import segun documen tenemos capacidad de automatizar
        # el proceso que queriamos