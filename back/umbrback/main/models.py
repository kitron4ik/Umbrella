from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Пользователи должны иметь email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



class Reg(AbstractBaseUser):
    regname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role_code = models.IntegerField()  
    building_code = models.IntegerField()  
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['regname', 'role_code', 'building_code', 'role']

    objects = CustomUserManager()

    class Meta:
        db_table = "reg"

    def __str__(self):
        return self.regname
