# Generated by Django 3.2.9 on 2021-12-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camnang',
            fields=[
                ('camnang_id', models.CharField(default='', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('camnang_name', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=100)),
                ('view', models.PositiveIntegerField(default='')),
                ('date', models.DateField()),
                ('decription', models.CharField(default='', max_length=200)),
            ],
        ),
    ]