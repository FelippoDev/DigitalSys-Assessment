# Generated by Django 4.2.4 on 2023-08-31 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposalfieldconfiguration',
            name='is_displayed',
        ),
    ]
