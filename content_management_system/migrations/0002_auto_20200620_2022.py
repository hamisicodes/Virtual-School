# Generated by Django 3.0.6 on 2020-06-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='user',
            new_name='author',
        ),
    ]
