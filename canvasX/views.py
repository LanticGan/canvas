from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import UserLoginForm, SignUpForm, ChangePasswardForm
from .models import MyUser, Student, Zipcode, Enrolls, Course, Section, Professor, Prof_team_members, Homework, \
    Homework_grades, Exams, Exam_grades


# Create your views here.


def home(request):
    isLogin = request.user.is_authenticated
    if isLogin:
        email = request.user.email
        user = MyUser.objects.get(email=email)
        # student courses
        if user.is_student == '1':
            # get all taking courses
            enrolls = Enrolls.objects.filter(student_email=email)
            full_name = Student.objects.get(user__email=email).name
            course_list = []
            for enroll in enrolls:
                course_info = dict()
                # get basic information of course
                course_id = enroll.course_id_id
                course_info['Course_id'] = course_id
                sec_no = enroll.section_no
                course_info['Course_section'] = sec_no
                course = Course.objects.get(course_id=course_id)
                course_name = course.course_name
                course_info['Course_name'] = course_name
                course_des = course.course_description
                course_info["Course_description"] = course_des

                # section info
                section = Section.objects.get(course_id=course_id, sec_no=sec_no)
                prof_team_id = section.prof_team_id
                section_type = section.section_type
                course_info["Course_section_type"] = section_type
                # get all professor information
                professors = Prof_team_members.objects.filter(team_id=prof_team_id)
                professor_list = []
                for prof in professors:
                    one_professor = dict()
                    one_professor["email"] = prof.prof_email_id
                    one_professor["office"] = Professor.objects.get(user=prof.prof_email).office_address
                    professor_list.append(one_professor)
                course_info["Professors"] = professor_list

                # get all homeworks
                homeworks = Homework.objects.filter(course_id=course_id, sec_no=sec_no)
                homework_list = []
                for h in homeworks:
                    one_homework = dict()
                    one_homework["Homework_number"] = h.hw_no
                    one_homework["Homework_detail"] = h.hw_detail
                    one_homework["Homework_grade"] = Homework_grades.objects.get(student_email=email,
                                                                                 course_id=course_id, sec_no=sec_no,
                                                                                 hw_no=h.hw_no).grades
                    homework_list.append(one_homework)
                course_info["Homeworks"] = homework_list

                # if the section type is Reg
                # get all exams
                if section_type == "Reg":
                    exams = Exams.objects.filter(course_id=course_id, sec_no=sec_no)
                    exam_list = []
                    for e in exams:
                        one_exam = dict()
                        one_exam["Exam_number"] = e.exam_no
                        one_exam["Exam_detail"] = e.exam_details
                        one_exam["Exam_grade"] = Exam_grades.objects.get(student_email=email, course_id=course_id,
                                                                         sec_no=sec_no, exam_no=e.exam_no).grades
                        exam_list.append(one_exam)
                    course_info["Exams"] = exam_list
                # else the section type is Cap
                # team number, mentor contact information and other team members information
                else:
                    team_id = 0
                course_list.append(course_info)
            return render(request, "user_information.html", {"course_list": course_list, "full_name": full_name})



        elif user.is_student == '0':
            professor = Professor.objects.get(user=email)
            professorInfo = {}
            professorInfo['name'] = professor.name
            professorInfo['age'] = professor.age
            professorInfo['gender'] = professor.office_address
            professorInfo['department'] = professor.department
            professorInfo['title'] = professor.title
            prof_team_member = Prof_team_members.objects.get(prof_email_id=professor.user_id)
            prof_team_id = prof_team_member.team_id_id
            sections = Section.objects.filter(prof_team_id_id=prof_team_id)

            sectionsInfo = []
            for section in sections:
                sectionItem = {}
                sectionItem['sec_no'] = section.sec_no
                sectionItem['section_type'] = section.section_type
                sectionItem['limit'] = section.limit
                sectionsInfo.append(sectionItem)

                course = Course.objects.get(course_id=section.course_id_id)
                sectionItem['course_name'] = course.course_name
                sectionItem['course_id'] = course.course_id

                homeworks = Homework.objects.filter(sec_no=section.sec_no, course_id_id=section.course_id_id)
                exams = Exams.objects.filter(sec_no=section.sec_no, course_id_id=section.course_id_id)

                homeworksList = []
                for homework in homeworks:
                    homeworkItem = {}
                    homeworkItem['hw_no'] = homework.hw_no
                    homeworkItem['hw_detail'] = homework.hw_detail
                    homeworksList.append(homeworkItem)

                examsList = []
                for exam in exams:
                    examItem = {}
                    examItem['exam_no'] = exam.exam_no
                    examItem['exam_detail'] = exam.exam_details
                    examsList.append(examItem)

                sectionItem['homeworksList'] = homeworksList
                sectionItem['examsList'] = examsList

            context = {}
            context['professorInfo'] = professorInfo
            context['sectionsInfo'] = sectionsInfo
            return render(request, "staff_information.html", context)

    else:
        return redirect('login')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    else:
        return render(request, "login.html", {'form': UserLoginForm()})


def signup(request):
    if request.method == 'POST':
        print(request)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def simulate(request):
    pass


def change_passward(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            password = request.POST['password']
            u = MyUser.objects.get(email=request.user.email)
            u.set_password(password)
            u.save()
        return redirect('login')
    else:
        return render(request, "changepwd.html", {'form': ChangePasswardForm()})
