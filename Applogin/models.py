from django.db import models

# Create your models here.

class RegistrarPersonas(models.Model):
    username = models.CharField(max_length=10)
    correo = models.EmailField(max_length=25)
    password = models.CharField()