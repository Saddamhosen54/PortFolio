# Generated by Django 4.2.16 on 2024-09-21 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
