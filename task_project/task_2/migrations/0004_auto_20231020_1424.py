# Generated by Django 2.2 on 2023-10-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_2', '0003_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteusers',
            name='email',
            field=models.EmailField(default='email', max_length=254),
        ),
        migrations.AddField(
            model_name='noteusers',
            name='first_name',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AddField(
            model_name='noteusers',
            name='last_name',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AddField(
            model_name='noteusers',
            name='password1',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AddField(
            model_name='noteusers',
            name='username',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='noteusers',
            name='password2',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]