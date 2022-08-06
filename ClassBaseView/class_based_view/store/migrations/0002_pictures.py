# Generated by Django 4.0.5 on 2022-07-14 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('picture', models.FileField(upload_to='picture/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.books')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
