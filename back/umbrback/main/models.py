from django.db import models

# Create your models here.
class login(models.Model):
    fio = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rolecode = models.IntegerField(max_length=100)
    buildcode = models.IntegerField(max_length=100)
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

