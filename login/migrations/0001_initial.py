# Generated by Django 3.2.9 on 2021-11-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
