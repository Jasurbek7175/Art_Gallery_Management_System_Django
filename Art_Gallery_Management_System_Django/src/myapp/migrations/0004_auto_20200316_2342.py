# Generated by Django 3.0.4 on 2020-03-16 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_mycart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 23, 42, 26, 117785)),
        ),
        migrations.DeleteModel(
            name='MyOrder',
        ),
    ]