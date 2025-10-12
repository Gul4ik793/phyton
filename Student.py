from subject import mathematics, biology, chemistry, russianlanguage
from faculty import FMIIIT_faculty, Chemistry_faculty, Philology_faculty, Biochemistry_faculty
from group import Group_22B, Group_33R, Group_11M
from speciality import chemistrys, mathematics_and_mechanics, literary_criticism, biological_sciences
from teacher import Yakovlev_teacher, Petrov_teacher, Sidorov_teacher, Hasanov_teacher


class Student:
    student_id = 0

    @classmethod
    def autoincrement(cls):
        cls.student_id += 1
        return cls.student_id

    def __init__(self, firstname, lastname, phone, stn, faculty, budget, speciality, group, patronymic = None, subject = None):
        self.__id = Student.autoincrement()
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.phone = phone
        self.__student_ticket_N = stn
        self.__faculty = faculty
        self.__budget = budget
        self.__speciality = speciality
        self.__group = group
        if subject is None:
            self.subject = list()
        else:
            self.subject = subject

    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"Cтудент № {self.__id}: [{self.firstname} {self.lastname}, {self.subject}]"

VasyaIvanov = Student(firstname="Вася",
                      lastname="Иванов",
                      phone="8-919-11-22-333",
                      stn="45690",
                      faculty=FMIIIT_faculty,
                      speciality=mathematics_and_mechanics,
                      group=Group_11M,
                      budget=True,
                      subject=[{"Предмет": russianlanguage, "преподаватель": Yakovlev_teacher, "оценка": 4.0},
                               {"Предмет": biology, "преподаватель": Petrov_teacher, "оценка": 4.0},
                               {"Предмет": mathematics, "преподаватель": Sidorov_teacher, "оценка": 5.0},
                               {"Предмет": chemistry, "преподаватель": Hasanov_teacher, "оценка": 3.0}])

KostyaPetrov = Student(firstname="Костя",
                      lastname="Петров",
                      phone="8-919-11-22-444",
                      stn="4578",
                      faculty=Biochemistry_faculty,
                      speciality=biological_sciences,
                      group=Group_22B,
                      budget=True,
                      subject=[{"Предмет": russianlanguage, "преподаватель": Yakovlev_teacher, "оценка": 4.0},
                               {"Предмет": biology, "преподаватель": Petrov_teacher, "оценка": 5.0},
                               {"Предмет": mathematics, "преподаватель": Sidorov_teacher, "оценка": 4.0},
                               {"Предмет": chemistry, "преподаватель": Hasanov_teacher, "оценка": 4.0}])
OlgaPetrova = Student(firstname="Ольга",
                      lastname="Петрова",
                      phone="8-919-11-22-555",
                      stn="7799",
                      faculty=Philology_faculty,
                      speciality=literary_criticism,
                      group=Group_33R,
                      budget=True,
                      subject=[{"Предмет": russianlanguage, "преподаватель": Yakovlev_teacher, "оценка": 5.0},
                               {"Предмет": biology, "преподаватель": Petrov_teacher, "оценка": 4.0},
                               {"Предмет": mathematics, "преподаватель": Sidorov_teacher, "оценка": 4.0},
                               {"Предмет": chemistry, "преподаватель": Hasanov_teacher, "оценка": 4.0}])

DaryaPetrova = Student(firstname="Дарья",
                      lastname="Петрова",
                      phone="8-919-11-22-556",
                      stn="7799",
                      faculty=Philology_faculty,
                      speciality=literary_criticism,
                      group=Group_33R,
                      budget=True,
                      subject=[{"Предмет": russianlanguage, "преподаватель": Yakovlev_teacher, "оценка": 5.0},
                               {"Предмет": biology, "преподаватель": Petrov_teacher, "оценка": 4.0},
                               {"Предмет": mathematics, "преподаватель": Sidorov_teacher, "оценка": 4.0},
                               {"Предмет": chemistry, "преподаватель": Hasanov_teacher, "оценка": 4.0}])

#print(VasyaIvanov.get_id(), KostyaPetrov.get_id(), OlgaPetrova.get_id())
#print(KostyaPetrov)
#print(KostyaPetrov.subject)
#print(OlgaPetrova.subject)


