# Generated by Django 4.0 on 2022-04-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='paragraph',
            field=models.TextField(max_length=500),
        ),
    ]
