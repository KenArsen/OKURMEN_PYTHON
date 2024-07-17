"""
Генератор - итератор, элементы которого можно итерировать только один раз

Итератор - объект, который поддерживает функцию next()

Итерируемый объект - объект, который предоставляет возможность обойти
поочередно свои элементы
"""


def gen(text):
    for word in text:
        yield word.upper()


a = gen(["apple", "banana", "cherry"])
try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print("Stop Iteration")
