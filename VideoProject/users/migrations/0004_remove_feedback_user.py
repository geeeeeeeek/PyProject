# Generated by Django 2.1.1 on 2018-12-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]