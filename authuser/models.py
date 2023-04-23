from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ROLES = (
    ('ADMIN', 'Administrateur'),
    ('SERVEUSE', 'Serveuse/Serveur'),
    ('CORDON_BLEU', 'Cordon bleu'),
    ('CLIENT', 'Client')
)
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    role = models.CharField(max_length=45, choices=ROLES, default='CLIENT')

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.username