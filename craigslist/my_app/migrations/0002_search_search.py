# Generated by Django 2.2.5 on 2019-12-29 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='search',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
