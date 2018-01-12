# Generated by Django 2.0.1 on 2018-01-12 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoicing', '0001_initial'),
        ('billing', '0002_auto_20180112_1151'),
        ('employees', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('entry_date', models.DateField()),
                ('description', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('overtime', models.FloatField()),
                ('is_billable', models.BooleanField()),
                ('bill_rate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='billing.BillRate')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='employees.Employee')),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='EntryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Entry Status',
                'verbose_name_plural': 'Entry Statuses',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='entries.EntryStatus'),
        ),
        migrations.AddField(
            model_name='entry',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='invoicing.Invoice'),
        ),
        migrations.AddField(
            model_name='entry',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='employees.Office'),
        ),
        migrations.AddField(
            model_name='entry',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_edtries', to='entries.Entry'),
        ),
        migrations.AddField(
            model_name='entry',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='tasks.Task'),
        ),
    ]