from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Kullanıcı modeline ekstra alanlar eklemek
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField("Biography", blank=True, null=True)

    # Varsayılan kullanıcı modeli zaten username, email, first_name, last_name gibi alanları içerir.
    
    def __str__(self):
        return self.username