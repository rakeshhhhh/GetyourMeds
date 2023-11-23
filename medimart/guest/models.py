from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class CommonTable(AbstractUser):
    city = models.CharField(
        max_length=50,
        default=''
    )
    place = models.CharField(
        max_length=50,
        default=''
    )
    phone = models.BigIntegerField(default=0)
    user_type = models.CharField(
        max_length=30,
        default='admin'
    )
    pin_code = models.IntegerField(
        default=0
    )

class ShopTable(models.Model):
    name = models.CharField(
        max_length=50,
    )
    latitude = models.CharField(
        max_length=100
    )
    longitude = models.CharField(
        max_length=100
    )
    open_on = models.TimeField()
    closed_on = models.TimeField()
    shop = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )

