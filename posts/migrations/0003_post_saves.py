# Generated by Django 5.0.6 on 2024-09-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='saves',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]