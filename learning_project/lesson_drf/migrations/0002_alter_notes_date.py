# Generated by Django 4.1 on 2023-11-15 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_drf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 11, 15, 18, 58, 45, 357436, tzinfo=datetime.timezone.utc)),
        ),
    ]
