# Generated by Django 2.1.7 on 2019-04-22 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0011_auto_20190422_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prof_team_members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasX.Professor')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasX.Prof_teams')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='prof_team_members',
            unique_together={('prof_email', 'team_id')},
        ),
    ]
