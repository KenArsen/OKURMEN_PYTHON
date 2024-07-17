"""
annotations >= Python 3.5
Для удобства восприятия стороннего кода.
Для удобства редактирования кода, когда IDE «подсказывает» атрибуты указанного типа переменных.
Для отслеживания некоторых явных ошибок на уровне несоответствия типов.
"""

"""
Expected type 'int', got 'str' instead
Ожидаемый тип «int», вместо этого получен «str»
"""

"""
int, float, str, bool
"""

"""
version >= Python 3.9 
list, tuple, dict, set
list[int], list[str], list[float], list[bool], list[None]
tuple[int, str, float, bool, ....], tuple[str], tuple[float], tuple[bool]
set[int], set[str], set[float], set[bool]
dict[str, int], dict[str, int], dict[str, float], dict[str, bool]

version < Python 3.9
from typing import List, Tuple, Dict, Set

начиная с версии Python 3.10, эту же нотацию можно определить и так
list[int | float]

"""

# def mul(x: int, y: int) -> int:
#     """
#     :param x:
#     :param y:
#     :return: x * y
#     """
#     return x * y
#
# print(mul(5, 3))
# print(mul.__annotations__)

from typing import List, Tuple, Dict, Set

def get_info(name: str, age: int) -> str:
    print(name)
    print(age)
    return f'{name} is {age} years old'

print(get_info.__annotations__)

def get_sum(nums: dict[int, str]) -> int:
    return sum(nums)


get_sum({1: "one", 2: "two"})



get_info("Arsen", 4)


