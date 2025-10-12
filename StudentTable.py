from Student import VasyaIvanov, KostyaPetrov, OlgaPetrova, Student, DaryaPetrova
from faculty import FMIIIT_faculty, Chemistry_faculty, Philology_faculty, Biochemistry_faculty
from group import Group_22B, Group_33R, Group_11M
from speciality import chemistrys, mathematics_and_mechanics, literary_criticism, biological_sciences
from subject import russianlanguage, mathematics, biology, chemistry
from teacher import Yakovlev_teacher, Petrov_teacher, Sidorov_teacher, Hasanov_teacher


class StudentTable:
    def __init__(self, name = "Список студентов", list_student = None):
        self.name = name
        if list_student is None:
            self.list_student = []
        else:
            self.list_student = list_student

    def add_student(self, student):
        if list_student is None:
            self.list_student = []
        else:
            return self.list_student.append(student)

    def set_student(self, student, student_new):
        if list_student is None:
            self.list_student = []
        else:
            if student in self.list_student:
                n = self.list_student.index(student)
                self.list_student[n] = student_new
            else:
                print(f"Ошибка, студент {student} не найден в списке студентов")

    def del_student(self, student):
        if list_student is None:
            self.list_student = []
        else:
            if student in self.list_student:
                self.list_student.remove(student)
            else:
                print(f"Ошибка, студент {student} не найден в списке студентов")

    def get_student(self):
        return self.list_student

    def search_student(self, search_term):
        result = []
        for student in self.list_student:
            name = f"{student.firstname} {student.lastname}".lower()
            if search_term.lower() in student.lastname.lower() or search_term.lower() in name:
                result.append(student)
        return result


class TeacherTable:
    def __init__(self, name = "Список преподавателей", list_teacher = None):
        self.name = name
        if list_teacher is None:
            self.list_teacher = []
        else:
            self.list_teacher = list_teacher

    def add_teacher(self, teacher):
        if list_teacher is None:
            self.list_teacher = []
        else:
            return self.list_teacher.append(teacher)

    def set_teacher(self, teacher, teacher_new):
        if list_teacher is None:
            self.list_teacher = []
        else:
            if teacher in self.list_teacher:
                n = self.list_teacher.index(teacher)
                self.list_teacher[n] = teacher_new

    def del_teacher(self, teacher):
        if list_teacher is None:
            self.list_teacher = []
        else:
            if teacher in self.list_teacher:
                self.list_teacher.remove(teacher)

    def get_teacher(self):
        return self.list_teacher

class FacultyTable:
    def __init__(self, name = "Список акультетов", list_faculty = None):
        self.name = name
        if list_faculty is None:
            self.list_faculty = []
        else:
            self.list_faculty = list_faculty

    def add_faculty(self, teacher):
        if list_faculty is None:
            self.list_faculty = []
        else:
            return self.list_faculty.append(teacher)

    def del_faculty(self, faculty):
        if list_faculty is None:
            self.list_faculty = []
        else:
            if faculty in self.list_faculty:
                self.list_faculty.remove(faculty)

    def get_faculty(self):
        return self.list_faculty


class GroupTable:
    def __init__(self, name = "Список акультетов", list_group = None):
        self.name = name
        if list_group is None:
            self.list_group = []
        else:
            self.list_group = list_group

    def add_group(self, teacher):
        if list_group is None:
            self.list_group = []
        else:
            return self.list_group.append(teacher)

    def del_group(self, group):
        if list_group is None:
            self.list_group = []
        else:
            if group in self.list_group:
                self.list_group.remove(group)

    def get_group(self):
        return self.list_group


list_student = StudentTable()
list_student.add_student(VasyaIvanov)
list_student.add_student(KostyaPetrov)
list_student.add_student(OlgaPetrova)
list_student.add_student(DaryaPetrova)
print(list_student.get_student())


results = list_student.search_student("Петрова")
print("результат поиска по фамилии", results)

list_teacher = TeacherTable()
list_teacher.add_teacher(Petrov_teacher)
list_teacher.add_teacher(Sidorov_teacher)
list_teacher.add_teacher(Yakovlev_teacher)
list_teacher.add_teacher(Hasanov_teacher)
print(list_teacher.get_teacher())

list_faculty = FacultyTable()
list_faculty.add_faculty(FMIIIT_faculty)
list_faculty.add_faculty(Biochemistry_faculty)
list_faculty.add_faculty(Chemistry_faculty)
list_faculty.add_faculty(Philology_faculty)
print(list_faculty.get_faculty())

list_group =GroupTable()
list_group.add_group(Group_11M)
list_group.add_group(Group_22B)
list_group.add_group(Group_33R)
print(list_group.get_group())

list_student.del_student(VasyaIvanov)
print(list_student.get_student())

list_teacher.del_teacher(Petrov_teacher)
print(list_teacher.get_teacher())

list_faculty.del_faculty(Chemistry_faculty)
print(list_faculty.get_faculty())

list_group.del_group(Group_11M)
print(list_group.get_group())

print(KostyaPetrov.phone)
KostyaPetrov_new = KostyaPetrov.phone = "8-919-11-22-111"
list_student.set_student(KostyaPetrov, KostyaPetrov_new)
print(KostyaPetrov.phone)

print(Hasanov_teacher.firstname)
Hasanov_teacher_new = Hasanov_teacher.firstname = "Василий"
list_student.set_student(Hasanov_teacher, Hasanov_teacher_new)
print(Hasanov_teacher.firstname)

#print(VasyaIvanov.get_id(), KostyaPetrov.get_id(), OlgaPetrova.get_id())
#print(KostyaPetrov.subject)
#print(OlgaPetrova.subject)

