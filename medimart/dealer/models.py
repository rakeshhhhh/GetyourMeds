from django.db import models
from guest.models import CommonTable


# Create your models here.

class MedicineTable(models.Model):
    ch = (
        ('available', 'available'),
        ('not available', 'not available')
    )
    id = models.BigAutoField(
        primary_key=True
    )
    code = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=50
    )
    mf_name = models.CharField(
        max_length=50,
        verbose_name='Manufacturer Name'
    )
    price = models.FloatField(
        default=0
    )
    image = models.FileField(
        upload_to='Medicines',
        max_length=300
    )
    status = models.CharField(
        choices=ch,
        max_length=50
    )
    dealer = models.ForeignKey(
        to=CommonTable,
        on_delete=models.CASCADE
    )
