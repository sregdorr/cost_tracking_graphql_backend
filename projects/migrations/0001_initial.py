# Generated by Django 2.0.1 on 2018-01-15 16:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('requires_afe', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='clients.Client')),
                ('lead_employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='employees.Employee')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='employees.Office')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Statuses',
            },
        ),
        migrations.CreateModel(
            name='ProjectSubset',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_subset_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_subsets', to='projects.Project')),
                ('project_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_subsets', to='clients.Contact')),
            ],
            options={
                'verbose_name': 'Project Subset',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Project Type',
            },
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('work_order_number', models.CharField(max_length=50)),
                ('limit', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
            ],
            options={
                'verbose_name': 'Work Order',
            },
        ),
        migrations.AddField(
            model_name='projectsubset',
            name='work_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_subsets', to='projects.WorkOrder'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='projects.ProjectStatus'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='projects.ProjectType'),
        ),
        migrations.AddField(
            model_name='project',
            name='work_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='projects.WorkOrder'),
        ),
    ]
