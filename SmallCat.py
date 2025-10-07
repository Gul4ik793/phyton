from Cat import Cat

class SmallCat(Cat):
    def __init__(self):
        self.name = "мелкий кот"

    def et_eat(self):
        return (f"Я {self.name}, я ем мало!")

    def et_sleep(self):
        return (f"Я {self.name}, я сплю чуть-чуть!")

    def et_run(self):
        return (f"Я {self.name}, я бегаю медленно!")


