# Generated by Django 2.2 on 2023-10-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='Date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]