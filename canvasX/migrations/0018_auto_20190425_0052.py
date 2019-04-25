# Generated by Django 2.1.7 on 2019-04-24 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canvasX', '0017_auto_20190424_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_no', models.IntegerField()),
                ('exam_no', models.IntegerField()),
                ('grades', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasX.Course')),
                ('student_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasX.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_no', models.IntegerField()),
                ('exam_no', models.IntegerField()),
                ('exam_details', models.CharField(max_length=200)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canvasX.Course')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='exams',
            unique_together={('course_id', 'sec_no', 'exam_no')},
        ),
        migrations.AlterUniqueTogether(
            name='exam_grades',
            unique_together={('student_email', 'course_id', 'sec_no', 'exam_no')},
        ),
    ]
