# Generated by Django 4.0.5 on 2022-07-03 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('class_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.classes')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tests',
            },
        ),
        migrations.CreateModel(
            name='Test_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.students')),
                ('tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.tests')),
            ],
            options={
                'db_table': 'test_results',
            },
        ),
    ]
