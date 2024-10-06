# Generated by Django 4.2.16 on 2024-09-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='images/profile')),
            ],
        ),
    ]