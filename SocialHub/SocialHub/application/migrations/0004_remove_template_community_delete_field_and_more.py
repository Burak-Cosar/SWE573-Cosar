# Generated by Django 4.2.11 on 2024-04-19 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_template_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='community',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]