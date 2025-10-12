class Departament:
    departament_id = 0

    @classmethod
    def autoincrement(cls):
        cls.departament_id += 1
        return cls.departament_id

    def __init__(self, name):
        self.__id = Departament.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"{self.name}"

FMIIIT = Departament("Математики и информационных технологий")
Biochemistry = Departament("Биохимия")
Chemistry = Departament("Химический")
Philology = Departament("Филологический")