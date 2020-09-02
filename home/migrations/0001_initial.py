# Generated by Django 3.0.7 on 2020-07-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='imgs/')),
                ('about', models.TextField(max_length=255)),
                ('phnum', models.IntegerField()),
            ],
        ),
    ]
