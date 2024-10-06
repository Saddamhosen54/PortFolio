# Generated by Django 4.2.16 on 2024-09-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_education_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_url',
            field=models.URLField(default=''),
        ),
    ]
