class MutableString:
    def __init__(self, string):
        self.string = string

    def list_string(self, id, l):
        string = list(str(self.string))
        string[id] = l
        string_new ="".join(string)
        return string_new

mystr = MutableString("Мойтекст")

print("Мой текст после измнения", mystr.list_string(2, "я"))