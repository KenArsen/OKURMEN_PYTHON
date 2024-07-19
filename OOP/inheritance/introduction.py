"""
Ключевыми понятиями наследования являются подкласс и суперкласс.
Подкласс наследует от суперкласса все публичные атрибуты и методы.
Суперкласс еще называется базовым (base class) или родительским (parent class),
а подкласс - производным (derived class) или дочерним (child class).
"""


"""
class подкласс(суперкласс):
    методы_подкласса
"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.age}')



class Employee(Person):
    def __init__(self, first_name, last_name, age, work, salary):
        super().__init__(first_name, last_name, age)
        self.work = work
        self.salary = salary

    def info(self):
        super().info()
        print(f'{self.work}\n{self.salary}')


class Student(Person):
    def __init__(self, first_name, last_name, age, university,  student_number):
        super().__init__(first_name, last_name, age)
        self.university = university
        self.student_number = student_number

    def info(self):
        super().info()
        print(f'{self.university}\n{self.student_number}')


emp_1 = Employee("Arsen", "Kenzhegulov", 22, "IT", 100000)
emp_1.info()

st_1 = Student("Arsen", "Kenzhegulov", 22, "Manas", '2004.01033')
st_1.info()











