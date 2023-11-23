# Generated by Django 3.2 on 2021-05-08 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineTable',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mf_name', models.CharField(max_length=50, verbose_name='Manufacturer Name')),
                ('price', models.IntegerField(default=0)),
                ('image', models.FileField(max_length=300, upload_to='Medicines')),
                ('status', models.CharField(choices=[('available', 'available'), ('not available', 'not available')], max_length=50)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]