from  Сategory import Сategory
from Сategory import drinks, dairy_products


class Product:
    __product_id = 0

    @classmethod
    def autoincrement(cls):
        cls.__product_id += 1
        return cls.__product_id

    def __init__(self, name, price, category):
        self.product_id = Product.autoincrement()
        self.name = name
        self.__price = price
        self.category = category

    def __repr__(self):
        return f"Товар № {self.product_id} : наименование = {self.name}, цена = {self.__price} руб, категория = {self.category}"

    def get_price(self):
        return self.__price

    def change_price(self, price_new):
        if price_new <= 0:
            raise ValueError("Цена не может быть 0 или отрицательным числом")
        self.__price = price_new
        return self.__price


cheese = Product("Сыр", 200, dairy_products)
juice = Product("Сок", 150, drinks)
icecream = Product("Мороженное", 50, dairy_products)

