# Generated by Django 4.2.18 on 2025-02-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toExercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(null=True, unique=True, upload_to='images'),
        ),
    ]
