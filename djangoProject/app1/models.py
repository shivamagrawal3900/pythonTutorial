from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    dob = models.DateField(default="1991-01-01")

    def __str__(self):
        return f"{self.name} -> {self.phone}"
