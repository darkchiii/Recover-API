# Generated by Django 5.0.6 on 2024-07-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_parent_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
