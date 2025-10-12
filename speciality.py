class Speciality:
    speciality_id = 0

    @classmethod
    def autoincrement(cls):
        cls.speciality_id += 1
        return cls.speciality_id

    def __init__(self, name):
        self.__id = Speciality.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

mathematics_and_mechanics = Speciality("Математика и механика")
chemistrys = Speciality("Химия")
biological_sciences = Speciality("Биологические науки")
literary_criticism = Speciality("Литературоведение")
