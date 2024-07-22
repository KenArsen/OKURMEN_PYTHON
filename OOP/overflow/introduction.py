class Test:

    def __init__(self, name):
        self.name = name

    def add(self, a: int, b: int) -> int:
        print("first add")
        return a + b

    def add(self, a: float, b: float) -> float:
        print("second add")
        return a + b


t = Test('test')
print(t.add(1, 2))
print(t.add(3.45, 4.23))


