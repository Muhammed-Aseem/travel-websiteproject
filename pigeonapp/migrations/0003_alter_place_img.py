# Generated by Django 3.2.15 on 2022-10-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pigeonapp', '0002_alter_place_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
