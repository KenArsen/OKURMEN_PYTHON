"""
https://docs.python.org/3/library/index.html
import random
random.random() -> Она при каждом вызове выдает случайное значение в диапазоне [0.0; 1.0).

random.uniform(1, 5) -> Другая похожая функция uniform(a, b) также генерирует случайные значения,
                        но в диапазоне от a до b:

random.randint(-3, 7) -> Если нам нужно моделировать целочисленные случайные значения,
                        то можно использовать или функцию:
                        [-3; 7]

lst = [4, 5, 0, -1, 10, 76, 3]
random.choice(lst) -> random при работе с последовательностями
                        выбрать один элемент случайным образом

random.shuffle(lst) -> Следующая функция shuffle() перемешивает элементы списка случайным образом:
                        Причем, меняет сам список, поэтому работает только с изменяемыми коллекциями.

random.sample(lst, 3) -> sample() возвращает новый список с указанным числом неповторяющихся элементов,
                            выбранных случайным образом из списка:
                            Разумеется, максимальное число элементов не может превышать число элементов в списке lst.

"""


# tasks
"""
Подвиг 3. На вход программе подаются два натуральных числа a, b (a < b), записанные через пробел. 
Прочитайте их и выполните генерацию целочисленной случайной величины в диапазоне [a; b]. 
Выведите результат на экран.

Ликбез: квадратная скобка - граница включается в диапазон; 
        круглая скобка - граница исключается из диапазона.
"""
# import random
# a, b = map(int, input().split())
# if a > b:
#     print("b > a")
# else:
#     print(random.randint(a, b))

"""
На вход программе подается строка с названиями городов, записанных через пробел. 
Прочитайте эту строку, сформируйте список из названий городов и выберите из этого списка один город случайным образом. 
Отобразите выбранный город на экране.
"""
import random
cities = [i for i in input().split()]
count = int(input())
print(random.sample(cities, count))
int()


"""
На вход программе подается строка с именами студентов, записанными через пробел. 
Требуется прочитать эти имена и случайным образом выбрать трех студентов из этого списка, используя функцию sample. 
(Полагается, что в исходном списке более трех студентов). 
Результат вывести на экран в одну строчку через пробел.
"""


