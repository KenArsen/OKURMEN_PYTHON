class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            print("Sorry, the age cannot be negative")
        else:
            self.__age = age



person_1 = Person("John", 25)
print(person_1.age)
person_1.age = 22
print(person_1.age)


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color in ['blue', 'black', 'white']:
            self.__color = color
        else:
            print("Sorry, the color must be blue, black or white")
            print(f"The dog color can't be {color}")


dog_1 = Dog("John", 25, "blue")
print(dog_1.color)
dog_1.color = "black"
print(dog_1.color)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def _get_pi(self):
        return 3.14


    def area(self):
        return self._get_pi() * self.radius ** 2

    def perimeter(self):
        return 2 * self._get_pi() * self.radius

# _
# <name>_
# _<name>
# __<name>
# __<name>__

from math import sin

sin_ = "Sinus"
print(sin(1))






