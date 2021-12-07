# Generated by Django 3.1.12 on 2021-12-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0009_auto_20210517_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='authLogin',
            fields=[
                ('username', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('userid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
