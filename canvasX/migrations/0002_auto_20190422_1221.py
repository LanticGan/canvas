# Generated by Django 2.1.7 on 2019-04-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]