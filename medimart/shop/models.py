from django.db import models
from django.db.models.deletion import CASCADE
from dealer.models import MedicineTable
from guest.models import CommonTable

# Create your models here.

class RequestTable(models.Model):
    qty = models.IntegerField(default=0)
    date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        default=0
    )
    price = models.FloatField(
        default=0
    )
    medicine = models.ForeignKey(
        to=MedicineTable,
        on_delete=models.CASCADE
    )
    shop = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )

class ReviewTable(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=300
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    rating = models.FloatField(
        default=0.0
    )
    customer = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )
    shop_med = models.ForeignKey(
        to=RequestTable,
        on_delete=models.CASCADE
    )

class CartTable(models.Model):
    qty = models.IntegerField(
        default=0
    )
    customer = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to=RequestTable,
        on_delete=models.CASCADE
    )

class OrderTable(models.Model):
    date = models.DateTimeField(
        auto_now_add=True
    )
    qty = models.FloatField()
    total = models.FloatField()
    status = models.IntegerField(
        default=0
    )
    product = models.ForeignKey(
        to=RequestTable,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )

