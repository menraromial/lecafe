from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

# Create your models here.
ROLES = (
    ('ADMIN', 'Administrateur'),
    ('SERVEUSE', 'Serveuse/Serveur'),
    ('CORDON_BLEU', 'Cordon bleu'),
    ('CLIENT', 'Client')
)

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('Users must have a password.')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):

        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.role = 'ADMIN'
        user.is_staff = True
        user.save(using=self._db)

        return user
 
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=45, choices=ROLES, default='CLIENT')

    objects = UserManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.username