# Generated by Django 3.0.6 on 2020-06-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
