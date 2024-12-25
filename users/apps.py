from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'User Management'

    def ready(self):
        # Burada uygulamanın hazır olduğunda yapılacak işlemler yer alabilir.
        # Örneğin, sinyalleri burada import edebilir ve bağlayabilirsiniz.
        pass