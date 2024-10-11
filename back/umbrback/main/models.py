from django.db import models


class login(models.Model):
    fio = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rolecode = models.IntegerField()  # Убрали max_length
    buildcode = models.IntegerField()  # Убрали max_length
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


