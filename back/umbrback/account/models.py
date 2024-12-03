from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Хеширует пароль
        user.save(using=self._db)
        return user

class RegUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (('doctor', 'Doctor'),('patient', 'Patient'),)
    regname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    role_code = models.IntegerField(blank=True, null=True)
    building_code = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True, choices=ROLES)

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

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Указываем, что email будет использоваться для логина
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Здесь можно указать дополнительные обязательные поля

    objects = CustomUserManager()

    class Meta:
        db_table = "reg"

    def __str__(self):
        return self.email
