# Generated by Django 3.0.5 on 2020-04-30 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_diary', '0002_auto_20200428_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
