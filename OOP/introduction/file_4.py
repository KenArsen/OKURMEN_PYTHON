class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance


ob_1 = BankAccount('Bob', 100)

print(ob_1.get_name())
ob_1.set_name(name="Arsen")
print(ob_1.balance)
ob_1.balance = 200
