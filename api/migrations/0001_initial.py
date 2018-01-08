# Generated by Django 2.0.1 on 2018-01-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('zip', models.CharField(max_length=15, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]