# Generated by Django 3.2.11 on 2022-01-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotb',
            name='date',
            field=models.DateField(default='2022-01-14'),
            preserve_default=False,
        ),
    ]