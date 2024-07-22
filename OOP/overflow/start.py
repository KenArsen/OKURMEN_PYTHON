class Overflow:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        obj = Overflow(self.value + other.value)
        return obj

    def __iadd__(self, other):
        self.value += other.value
        return self

ob_1 = Overflow(1)
ob_2 = Overflow(2)
ob_3 = ob_1 + ob_2
ob_1 += ob_2

print(ob_3.value)
print(ob_1.value)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f'{self.name} is {self.age}'


arsen = Person('Arsen', 22)
ali = Person('Ali', 15)
print(ali)
print(arsen)

if arsen > ali:
    print(True)
    print("Arsen chon")
else:
    print("Arsen chon emes")
    print(False)
