# Generated by Django 4.0 on 2022-04-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic2', '0002_alter_paragraph_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(max_length=100)),
                ('skill2', models.CharField(max_length=100)),
                ('skill3', models.CharField(max_length=100)),
            ],
        ),
    ]
