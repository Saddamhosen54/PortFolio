# Generated by Django 4.2.16 on 2024-09-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_skill_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='icon',
            field=models.CharField(blank=True, help_text='FontAwesome icon name or image URL', max_length=100),
        ),
        migrations.AddField(
            model_name='skill',
            name='proficiency_level',
            field=models.IntegerField(default= 0, help_text='Enter proficiency level as a percentage (0-100)'),
            preserve_default=False,
        ),
    ]