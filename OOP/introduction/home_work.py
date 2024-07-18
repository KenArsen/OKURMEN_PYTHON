"""
Dog деген класс жазыныздар
Анын name, age деген свойстволары жана
sleep, eat деген методдору болсун

Объект создание кылып ал обиектин
sleep деген методун чакырганда бизге '<name> the dog is sleeping'
деп чыгыш керек.
эгер eat методдун чакырсак анда '<name> the dog is eating'
деп чыгыш керек
"""

class Dog:
    name = ""
    age = 0

    def sleep(self):
        print(f"The dog {self.name} is sleeping")

    def eat(self):
        print(f"The dog {self.name} is eating")

dog1 = Dog()
dog1.name = "Simba"
dog1.age = 2
dog1.sleep()
dog1.eat()

dog2 = Dog()
dog2.name = "Baltek"
dog2.age = 3
dog2.sleep()
dog2.eat()