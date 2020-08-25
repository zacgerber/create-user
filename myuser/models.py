from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    age = models.IntegerField(null=True)
    homepage = models.URLField(null=True)

    REQUIRED_FIELD = ['age', 'homepage']

    def __str__(self):
        return self.username




