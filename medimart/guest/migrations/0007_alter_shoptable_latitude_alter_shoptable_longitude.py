# Generated by Django 4.0.4 on 2023-11-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_alter_shoptable_latitude_alter_shoptable_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoptable',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shoptable',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
    ]
