# Generated by Django 4.1.3 on 2022-11-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to='photos/%d/%m/%Y'),
        ),
    ]
