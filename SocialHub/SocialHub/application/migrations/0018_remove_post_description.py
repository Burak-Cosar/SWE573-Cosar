# Generated by Django 4.2.11 on 2024-05-10 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0017_community_invited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]
