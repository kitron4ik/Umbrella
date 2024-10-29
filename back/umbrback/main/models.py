from django.db import models


class RegUser(models.Model):
    regname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role_code = models.IntegerField()  
    building_code = models.IntegerField()  
    role = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    class Meta:
        db_table = "reg"

def __str__(self):
        return self.regname 
