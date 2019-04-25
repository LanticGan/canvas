from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManger(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=True
    )
    is_student = models.CharField(max_length=1, default='1')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_student']

    objects = CustomUserManger()

    def __str__(self):
        return self.email


class Zipcode(models.Model):
    zipcode = models.IntegerField(primary_key=True, unique=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=False, related_name="students",
                                primary_key=True)
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=40)
    gender = models.CharField(max_length=1)
    major = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    zipcode = models.ForeignKey(Zipcode, on_delete=models.CASCADE, default=0)


class Department(models.Model):
    dept_id = models.CharField(max_length=20, primary_key=True, unique=True)
    dept_name = models.CharField(max_length=50)
    dept_head = models.CharField(max_length=50)


class Professor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=False, related_name="faculty", primary_key=True)
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=1)
    office_address = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)


class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True, unique=True)
    course_name = models.CharField(max_length=100, null=False)
    course_description = models.CharField(max_length=100, null=False)


class Prof_teams(models.Model):
    team_id = models.IntegerField(primary_key=True, unique=True)


class Section(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=False)
    section_type = models.CharField(max_length=10, null=False)
    limit = models.IntegerField(null=False)
    prof_team_id = models.ForeignKey(Prof_teams, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ("course_id", "sec_no")


class Enrolls(models.Model):
    student_email = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_no = models.IntegerField()

    class Meta:
        unique_together = ('student_email', 'course_id')


class Prof_team_members(models.Model):
    prof_email = models.ForeignKey(Professor, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Prof_teams, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('prof_email', 'team_id')


class Homework(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=False)
    hw_no = models.IntegerField(null=False)
    hw_detail = models.CharField(max_length=200)

    class Meta:
        unique_together = ('course_id', 'sec_no', 'hw_no')


class Homework_grades(models.Model):
    student_email = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=False)
    hw_no = models.IntegerField(null=False)
    grades = models.IntegerField()

    class Meta:
        unique_together = ('student_email', 'course_id', 'sec_no', 'hw_no')


class Exams(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=False)
    exam_no = models.IntegerField(null=False)
    exam_details = models.CharField(max_length=200)

    class Meta:
        unique_together = ('course_id', 'sec_no', 'exam_no')


class Exam_grades(models.Model):
    student_email = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=False)
    exam_no = models.IntegerField(null=False)
    grades = models.IntegerField()

    class Meta:
        unique_together = ('student_email', 'course_id', 'sec_no', 'exam_no')


class Capstone_setion(models.Model):
   course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
   sec_no = models.IntegerField(null=False)
   project_no = models.IntegerField(null=False, unique=True, primary_key=True)
   sponsor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)


class Capstone_Team(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField(null=True)
    team_id = models.IntegerField(null=True, unique=True)
    project_id = models.ForeignKey(Capstone_setion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course_id', 'sec_no', 'team_id')


class Capstone_Team_Members(models.Model):
    student_email = models.ForeignKey(Student, on_delete=models.CASCADE)
    team_id = models.IntegerField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    project_no = models.ForeignKey(Capstone_setion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student_email', 'team_id', 'course_id', 'project_no')


class Capstone_grades(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sec_no = models.IntegerField()
    team_id = models.IntegerField()
    grade = models.IntegerField()

    class Meta:
        unique_together = ('team_id', 'course_id', 'sec_no')
