from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import sys



class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # autres champs spécifiques au client

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrateur'),
        ('manager', 'Gestionnaire'),
        ('employee', 'Employé'),
        ('driver', 'driver'),
    )

    role = models.CharField(max_length=20, choices=ROLES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, related_name='agents')

    def __str__(self):
        return self.username
    

