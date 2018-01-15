# Generated by Django 2.0.1 on 2018-01-15 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillableItem',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('is_billed_overtime', models.BooleanField()),
                ('is_default', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Billable Item',
            },
        ),
        migrations.CreateModel(
            name='BillRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('overtime_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'verbose_name': 'Bill Rate',
                'verbose_name_plural': 'Bill Rates',
            },
        ),
        migrations.CreateModel(
            name='BillType',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Bill Type',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('department_title', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
