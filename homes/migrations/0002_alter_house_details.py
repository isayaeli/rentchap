# Generated by Django 3.2.2 on 2021-07-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='details',
            field=models.TextField(),
        ),
    ]