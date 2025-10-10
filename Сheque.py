import datetime
import random
from Сategory import drinks, dairy_products
from Product import cheese, juice, icecream, Product


class Сheque:
    __check_number = 0
    _checksum_storage = {}

    @classmethod
    def autoincrement(cls):
        cls.__check_number += 1
        return cls.__check_number

    def __init__(self):
        self.__check_number = Сheque.autoincrement()
        self.date = datetime.datetime.now()
        self._checksum = self._generate_unique_checksum()
        self.products = []

    def _generate_unique_checksum(self) -> int:
        while True:
            checksum = random.randint(100000, 200000)
            if checksum not in Сheque._checksum_storage:
                Сheque._checksum_storage[checksum] = True
                return checksum

    def add_product(self, product: Product):
        self.products.append(product)

    def get_check_number(self) -> int:
        return self.__check_number

    def get_checksum(self) -> int:
        return self._checksum

    def __repr__(self):
        return (f"Чек номер № {self.__check_number}: дата чека = {self.date} сумма чека {self._checksum} продукты: {self.products}")

check = Сheque()




