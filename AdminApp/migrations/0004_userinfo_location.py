# Generated by Django 4.0.1 on 2022-11-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_paymentmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='location',
            field=models.CharField(default='Pune', max_length=20),
            preserve_default=False,
        ),
    ]