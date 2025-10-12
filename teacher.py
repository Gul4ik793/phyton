from department import FMIIIT, Biochemistry, Chemistry, Philology


class Teacher:
    teacher_id = 0

    @classmethod
    def autoincrement(cls):
        cls.teacher_id += 1
        return cls.teacher_id

    def __init__(self, firstname, lastname, phone, academic, department, patronymic = None):
        self.__id = Teacher.autoincrement()
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.phone = phone
        self.__academic = academic
        self.__department = department


    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"

Petrov_teacher = Teacher(firstname="Василий",
                         lastname="Петров",
                         phone="8-927-33-33-333",
                         academic="магистр",
                         department=Biochemistry)
Sidorov_teacher = Teacher(firstname="Иван",
                          lastname="Сидоров",
                          phone="8-927-44-44-444",
                          academic="магистр",
                          department=FMIIIT)
Yakovlev_teacher = Teacher(firstname="Сергей",
                          lastname="Яковлев",
                          phone="8-927-55-55-555",
                          academic="магистр",
                          department=Philology)
Hasanov_teacher = Teacher(firstname="Рустам",
                          lastname="Хасанов",
                          phone="8-927-66-66-666",
                          academic="магистр",
                          department=Chemistry)


