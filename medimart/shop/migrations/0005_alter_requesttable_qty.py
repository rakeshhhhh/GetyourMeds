# Generated by Django 3.2 on 2021-05-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_requesttable_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttable',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
