# Generated by Django 4.2.7 on 2024-02-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.CharField(max_length=20),
        ),
    ]
