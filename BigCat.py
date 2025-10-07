from Cat import Cat

class BigCat(Cat):
    def __init__(self):
        self.name = "большой кот"

    def et_eat(self):
        return (f"Я {self.name}, я ем много!")

    def et_sleep(self):
        return (f"Я {self.name}, я сплю долго!")

    def et_run(self):
        return (f"Я {self.name}, я бегаю быстро!")
