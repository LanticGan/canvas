# Generated by Django 2.1.7 on 2019-04-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0006_auto_20190422_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.CharField(max_length=100)),
            ],
        ),
    ]
