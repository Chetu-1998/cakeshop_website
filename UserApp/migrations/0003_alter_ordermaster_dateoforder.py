# Generated by Django 4.0.1 on 2022-11-24 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_ordermaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermaster',
            name='dateOfOrder',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]