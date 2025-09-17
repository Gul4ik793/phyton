from queue import Queue
Queue_Ivanov = Queue()
Queue_Petrov = Queue()

def add_my_Queue(doctor, patient):
    if doctor.name == ivanov_doctor.name:
        Queue_Ivanov.put(patient.name)
    else:
        if doctor.name == petrov_doctor.name:
            Queue_Petrov.put(patient.name)
        else:
            return ("Такого доктора нет")


def get_my_Queue_Ivanov():
    while not Queue_Ivanov.empty():
        return Queue_Ivanov.get()
    return ("В очереди пациентов нет")

def get_my_Queue_Petrov():
    while not Queue_Petrov.empty():
        return Queue_Petrov.get()
    return ("В очереди пациентов нет")

class Doctor:
    def __init__(self, name):
        self.name = name
        self.__list_name_patient = list()


    def add_patient(self, patient):
        self.__list_name_patient.append(patient)

    def get_patient(self):
        return [patient.name for patient in self.__list_name_patient]

    def get_unique_patient(self):
        return list(set(self.get_patient()))


class Patient:
    def __init__(self, name):
        self.name = name


class CommonPatient:
    def __init__(self, *args):
        self.doctors = [doctor for doctor in args]

    def get_doctors(self):
        return [doctor.name for doctor in self.doctors]

    def get_common_patient(self):
        sets_of_patients = [set(doctor.get_unique_patient()) for doctor in self.doctors]
        if not sets_of_patients:
            return []
        common_patients = set.intersection(*sets_of_patients)
        return list(common_patients)


ivanov_doctor = Doctor("Иванов")
petrov_doctor = Doctor("Петров")

sidorov_patient = Patient("Сидоров")
hasanov_patient = Patient("Хасанов")
sergeev_patient = Patient("Сергеев")
sharipov_patient = Patient("Шарипов")
zaripov_patient = Patient("Зарипов")

ivanov_doctor.add_patient(sidorov_patient)
ivanov_doctor.add_patient(sergeev_patient)
ivanov_doctor.add_patient(zaripov_patient)

print("Все посетители доктора Иванов:", ivanov_doctor.get_patient())
print("Уникальные посетители доктора Иванов:", ivanov_doctor.get_patient())

petrov_doctor.add_patient(zaripov_patient)
petrov_doctor.add_patient(hasanov_patient)
petrov_doctor.add_patient(sharipov_patient)
petrov_doctor.add_patient(sergeev_patient)

print("Все посетители доктора Петров:", petrov_doctor.get_patient())
print("Уникальные посетители доктора Петров:", petrov_doctor.get_patient())

CD = CommonPatient(ivanov_doctor, petrov_doctor)
print("Общие пациенты:", CD.get_common_patient())

add_my_Queue(ivanov_doctor, sidorov_patient)
add_my_Queue(ivanov_doctor, hasanov_patient)
add_my_Queue(ivanov_doctor, sharipov_patient)

add_my_Queue(petrov_doctor, sergeev_patient)


print(f"В очереди у доктора {ivanov_doctor.name} пациентов: {Queue_Ivanov.qsize()}")

print(f"В очереди у доктора {petrov_doctor.name} пациентов: {Queue_Petrov.qsize()}")

print(f"Следующий в очереди у доктора {ivanov_doctor.name}:", get_my_Queue_Ivanov())
print(f"Следующий в очереди у доктора {ivanov_doctor.name}:", get_my_Queue_Ivanov())
print(f"Следующий в очереди у доктора {ivanov_doctor.name}:", get_my_Queue_Ivanov())
print(f"Следующий в очереди у доктора {ivanov_doctor.name}:", get_my_Queue_Ivanov())
print(f"Следующий в очереди у доктора {petrov_doctor.name}:", get_my_Queue_Petrov())
print(f"Следующий в очереди у доктора {petrov_doctor.name}:", get_my_Queue_Petrov())
