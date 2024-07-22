class Shape:
    def __init__(self, x, y):
        self.x = x # атрибут объекта
        self.y = y # атрибут объекта

    def area(self):
        return self.x * self.y

    @staticmethod
    def info(a, b):
        print("This is a static method")
        print(a + b)


# Shape.info(3, 4)
# ob_1 = Shape(1, 2)
# ob_1.info(3, 4)
# print(ob_1.area())

class Counter:
    count = 0

    def __init__(self, name):
        self.name = name
        Counter.count += 1


    @staticmethod
    def get_count_objects():
        print(f"All objects = {Counter.count}")


obj1 = Counter("ob_1")
obj2 = Counter("ob_2")
Counter.get_count_objects()
obj3 = Counter("ob_3")
Counter.get_count_objects()

