from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # autres champs spécifiques au client

    def __str__(self):
        return self.name

class User(models.Model):
    ROLES = (
        ('admin', 'Administrateur'),
        ('manager', 'Gestionnaire'),
        ('employee', 'Employé'),
    )

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
