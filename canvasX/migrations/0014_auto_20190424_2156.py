# Generated by Django 2.1.7 on 2019-04-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0013_auto_20190424_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='department',
            field=models.CharField(default='', max_length=20),
        ),
    ]
