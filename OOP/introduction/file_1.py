# class Car:
#     name = ""
#     model = ""
#     year = 2024
#
#     def info(self):
#         print(f"Name: {self.name}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")
#
#
# car_1 = Car()
# car_1.name = "BMW"
# car_1.model = "N5"
# car_1.year = 2020
# car_1.info()
#
# car_2 = Car()
# car_2.name = "Toyata"
# car_2.model = "Camry"
# car_2.year = 2018
# car_2.info()
#
# car_3 = Car()
# car_3.name = "Tesla"
# car_3.model = "ModelX"
# car_3.year = 2023
# car_3.info()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f'{self.__name} is {self.__age}')


p1 = Person('John', 25)
p1.__name = "Arsen"
p1.__age = 25
p1.info()

