# Generated by Django 2.2.5 on 2020-06-23 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_diary', '0003_auto_20200430_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='health_diary.Post'),
        ),
    ]
