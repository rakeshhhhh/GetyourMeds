# Generated by Django 3.2 on 2021-05-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttable',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]