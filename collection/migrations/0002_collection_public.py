# Generated by Django 5.0.1 on 2024-08-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
