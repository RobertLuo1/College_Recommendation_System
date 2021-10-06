# Generated by Django 3.2.5 on 2021-07-21 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainJob',
            fields=[
                ('mainJobID', models.IntegerField(primary_key=True, serialize=False)),
                ('mainJobName', models.TextField()),
                ('mainJobCategory', models.IntegerField()),
            ],
            options={
                'verbose_name': '主职业',
                'db_table': 'MainJob',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.TextField()),
                ('salary', models.TextField()),
                ('mainJobID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapps.mainjob')),
            ],
            options={
                'verbose_name': '职业',
                'db_table': 'Job',
            },
        ),
    ]