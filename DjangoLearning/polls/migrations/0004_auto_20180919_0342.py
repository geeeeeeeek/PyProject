# Generated by Django 2.1.1 on 2018-09-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.CharField(max_length=100),
        ),
    ]
