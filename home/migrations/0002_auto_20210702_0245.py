# Generated by Django 3.2.2 on 2021-07-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
