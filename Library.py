class Library:
    def __init__(self, name, address, quantity = 0):
        self.name = name
        self.address = address
        self.quantity = quantity

    def __repr__(self):
        return (f"Библиотека {self.name}, по улице: {self.address} содержит {self.quantity} книг")

    def __add__(self, other):
        if other <= 0:
            raise ValueError("Неверно введено количество книг для добавления")
        return Library(self.name, self.address, self.quantity + other)

    def __sub__(self, other):
        if other <= 0:
            raise ValueError("Неверно введено количество книг для вычитания")
        if self.quantity - other < 0:
            raise ValueError(f"Нельзя вычесть! Kоличество книг в Библиотеке {self.name} меньше, чем {other}")
        return Library(self.name, self.address, self.quantity - other)

    def __iadd__(self, other):
        if other <= 0:
            raise ValueError("Неверно введено количество книг для добавления")
        self.quantity += other
        return self

    def __isub__(self, other):
        if other <= 0:
            raise ValueError("Неверно введено количество книг для вычитания")
        if self.quantity - other <= 0:
            raise ValueError(f"Нельзя вычесть! Kоличество книг в Библиотеке {self.name} меньше, чем {other}")
        self.quantity -= other
        return self

    def __lt__(self, other):
        return self.quantity < other.quantity

    def __gt__(self, other):
        return self.quantity > other.quantity

    def __le__(self, other):
        return self.quantity <= other.quantity

    def __ge__(self, other):
        return self.quantity >= other.quantity

    def __eq__(self, other):
        return self.quantity == other.quantity

    def __ne__(self, other):
        return self.quantity != other.quantity





