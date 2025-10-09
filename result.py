from Library import Library


lib = Library("Детская районная", "ул. Кирова, 45", 35)
print(lib)
lib = lib + 10
print(lib)
lib = lib - 40
print(lib)
lib += 50
print(lib)
lib -= 10
print(lib)
lib2 = Library("Взрослая", "ул. Достоевского, 100", 5)
print(lib2)
print(lib > lib2)
print(lib < lib2)
print(lib >= lib2)
print(lib <= lib2)
print(lib == lib2)
print(lib != lib2)