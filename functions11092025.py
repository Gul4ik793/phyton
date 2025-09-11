#ЗАДАЧА №1
def Age_sister(x, y):
    if (y == 0) or (y == 1):
        return ("Сестра не может быть ровесницей брата и брату не должно быть 0 лет")
    else:
         return (x * y / (y - 1))

age1 = Age_sister(6,3)
print("Сестре: ", age1, "лет")



#ЗАДАЧА №2
def Divisible_by_3_5(x):
    for i in range(x, 0, -1):
        if (i%3 == 0) and (i%5 == 0):
            print(i, ",", end='')

divisible1 = Divisible_by_3_5(100)
print(" - в обратном порядке только те числа из диапазона от 0 до 100, которые одновременно делятся на 3 и 5", divisible1)


#ЗАДАЧА №3
def Summ_N(N, M):
    f = str()
    h = 0
    for i in range(N):
        i += 1
        f = f + str(M)
        h = h + int(f)
    return(h)

summ1 = Summ_N(5, 3)
print("Сумма разрядов: ", summ1)


#ЗАДАЧА №4
def M_cycle(list):
    B = str()
    for i in range(len(list)):
        B = B + list[i-1]
    return (B)

main_cycl = M_cycle("567890")
print("Циклически сдвинты элементы списка вправо ", main_cycl)


#ЗАДАЧА №5
def M_list(lists):
    l = 0
    for i in range(len(lists)):
        x = lists[i]
        if l < lists.count(x):
            l = lists.count(x)
        else:
            i += 1
    return (x)

main_list = M_list("123233777777")
print("число", main_list, " в этом списке встречается чаще всего")


#ЗАДАЧА №6
def Elements(lists):
    return (len(list(set(lists))))

main_elements = Elements("123233777777")
print(main_elements, "различных элементов")







