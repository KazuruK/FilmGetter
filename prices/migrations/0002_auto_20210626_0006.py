# Generated by Django 3.2.4 on 2021-06-25 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iddb',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 6, 26)),
        ),
        migrations.AddField(
            model_name='iddb',
            name='detail',
            field=models.CharField(default='Found.', max_length=20),
        ),
    ]
