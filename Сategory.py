class Сategory:
    __category_id = 0

    @classmethod
    def autoincrement(cls):
        cls.__category_id += 1
        return cls.__category_id

    def __init__(self, category):
        self.category_id = Сategory.autoincrement()
        self.category = category

    def __repr__(self):
        return f" {self.category} (№{self.category_id})"

    def get_category_id(self):
        return self.__category_id

    def get_category(self):
        return self.category

dairy_products = Сategory("Молочные продукты")
drinks = Сategory("Напитки")


