# Generated by Django 4.1.7 on 2023-02-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_image_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image_model',
            field=models.ImageField(default='1.jpg', null=True, upload_to='images/'),
        ),
    ]
