# Generated by Django 4.1.6 on 2023-02-12 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geek_fit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='video',
        ),
    ]
