# Generated by Django 4.0.1 on 2022-01-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_car_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Prix'),
        ),
    ]
