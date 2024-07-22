class Animal:
    type = "dangerous" # атрибут класса
    def __init__(self, name):
        self.name = name # атрибут объекта


class Shape:
    def __init__(self, x, y):
        self.x = x # атрибут объекта
        self.y = y # атрибут объекта


ob_1 = Animal("Lion")
ob_2 = Animal("Tiger")
print(ob_1.type)
print(ob_2.type)
print(ob_1.name)
print(ob_2.name)
Animal.type = "DANGEROUS"
print(ob_1.type)
print(ob_2.type)
