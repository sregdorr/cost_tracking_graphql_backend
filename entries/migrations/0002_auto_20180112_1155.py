# Generated by Django 2.0.1 on 2018-01-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
