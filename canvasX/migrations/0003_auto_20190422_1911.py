# Generated by Django 2.1.7 on 2019-04-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0002_auto_20190422_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('zipcode', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='zipcode',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='canvasX.Zipcode'),
        ),
    ]
