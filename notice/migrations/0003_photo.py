# Generated by Django 2.2.5 on 2020-06-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20200527_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captiion', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='room_photos')),
            ],
        ),
    ]