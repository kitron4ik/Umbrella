from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class RegUser(AbstractUser):
    regname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role_code = models.IntegerField()
    building_code = models.IntegerField()  
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    groups = models.ManyToManyField(
        Group,
        related_name="reguser_set",  # Уникальное имя для обратной связи
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="reguser_permissions_set",  # Уникальное имя для обратной связи
        blank=True
    )

    
    class Meta:
        db_table = "reg"
        

def __str__(self):
        return self.regname 
