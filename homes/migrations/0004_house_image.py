# Generated by Django 3.2.2 on 2021-07-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_house_published_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='house_images'),
        ),
    ]