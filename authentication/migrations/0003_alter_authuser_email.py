# Generated by Django 3.2.20 on 2023-10-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20231006_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
    ]
