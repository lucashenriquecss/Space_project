# Generated by Django 4.1.3 on 2022-11-24 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%d/%m/%Y')),
                ('title', models.CharField(max_length=200)),
                ('categories', models.CharField(choices=[('Nebulosa', 'Nebulosa'), ('Planeta', 'Planeta'), ('Estrela', 'Estrela'), ('Galáxia', 'Galáxia')], default='Planeta', max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]