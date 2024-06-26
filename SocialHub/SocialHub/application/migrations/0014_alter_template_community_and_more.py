# Generated by Django 4.2.11 on 2024-04-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_template_community_alter_community_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='application.community'),
        ),
        migrations.AlterField(
            model_name='templatefield',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='application.template'),
        ),
    ]
