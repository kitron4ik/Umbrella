from django.db import models, IntegrityError
from django.db import connection

# Create your models here.
class Login(models.Model):
    regname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    role_code = models.IntegerField()
    building_code = models.IntegerField()
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.regname

def login_or_register(regname, email, role_code, building_code, role, password):
    try:
        user = Login.objects.get(email=email)
        print(f"Пользователь с email {email} уже существует. Выполняем вход.")
        return user
    except Login.DoesNotExist:
        try:
            user = Login.objects.create(
                regname=regname,
                email=email,
                role_code=role_code,
                building_code=building_code,
                role=role,
                password=password
            )
            print(f"Пользователь с email {email} успешно зарегистрирован.")
            return user
        except IntegrityError:
            print(f"Ошибка при регистрации пользователя с email {email}.")
            return None

def reg(regname, email, role_code, building_code, role, password):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO umbrella_reg (regname, email, role_code, building_code, role, password) VALUES (%s, %s, %s, %s, %s, %s)",
            [regname, email, role_code, building_code, role, password]
        )

# Пример использования функции
user = login_or_register("Иван Иванов", "ivan@example.com", 1, 1, "admin", "password123")

