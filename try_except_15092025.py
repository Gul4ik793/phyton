my_string = "123"
my_file = "Myfail10092025.txt"

with open(my_file, "w") as file:
    try:
        if my_string != "123":
            file.write(my_string)
            print(f"Cтрока {my_string} записана в файл: {my_file}")
        else:
            print("Ошибка, строка 123")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

