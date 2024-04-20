# Generated by Django 4.2.11 on 2024-04-20 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_defaultpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TemplateField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=255)),
                ('field_type', models.CharField(max_length=100)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='application.template')),
            ],
        ),
        migrations.RemoveField(
            model_name='community',
            name='default_template',
        ),
        migrations.DeleteModel(
            name='DefaultPost',
        ),
        migrations.DeleteModel(
            name='DefaultTemplate',
        ),
    ]
