from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionMixin

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """Create and save new User"""

        user = username
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create and save new superuser"""

        user = self.create_user(username, password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionMixin):
    """Custom model that support using USERNAME"""

    username = models.CharField(max_length=255, unique=True)
    Name = models.CharField(max_length=255)
    email = models.EmailField(max_legth=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'