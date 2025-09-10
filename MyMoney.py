class MyMoney:
    def __init__(self, lastname, firstname, balance):
        self.lastname = lastname
        self.firstname = firstname
        self.balance = balance


    def balance_up(self, balance):
        self.balance += balance
        return (self.balance)

    def balance_down(self, balance):
        if self.balance < balance:
            print ("Нельзя снять денег больше, чем в кошельке -None")
        else:
            self.balance = self.balance - balance
            return (self.balance)

    def get_balance(self):
        return (self.balance)

ivanov_money = MyMoney("Иванов", "Иван",0)
petrov_money = MyMoney("Петров", "Петр", 100)
print("первоначально баланс Иванова", ivanov_money.get_balance())
print("первоначально баланс Петрова", petrov_money.get_balance())
ivanov_money.balance_up(200)
petrov_money.balance_up(600)

print("баланс Иванова после увеличения", ivanov_money.get_balance())
print("баланс Иванова после увеличения", petrov_money.get_balance())

ivanov_money.balance_down(500)
petrov_money.balance_down(300)

print("баланс Иванова после уменьшения", ivanov_money.get_balance())
print("баланс Петрова после уменьшения", petrov_money.get_balance())
