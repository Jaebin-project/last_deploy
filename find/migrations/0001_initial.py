# Generated by Django 3.0.5 on 2020-04-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('zone_category', models.CharField(max_length=20)),
                ('info', models.TextField()),
                ('site_url', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=15)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('Hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='find.Hospital')),
            ],
        ),
    ]
