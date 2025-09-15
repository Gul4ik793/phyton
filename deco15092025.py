from timeit import Timer
import time
def deco(f):
    print("вызвана функция list_string()")
    return f
@deco


class MutableString:
    def __init__(self, string):
        self.string = string

    def list_string(self):
        string = list(str(self.string))
        string[2] = "я"
        string_new ="".join(string)
        return string_new

mystr = MutableString("Мойтекст")

t = Timer(stmt=mystr.list_string)
print("Время выполнения функции list_string():", t.timeit(number=1000))