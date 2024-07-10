"""
try:
    блок операторов
    критического кода
except [исключение]:
    блок операторов
    обработки исключения
finally:
    блок операторов
    всегда исполняемых
    вне зависимости, от
    возникновения исключения


Менеджер контекста для файлов
Так вот, в языке Python существует специальный оператор with, который,
можно воспринимать как аналог конструкции try / finally и в случае работы с файлами записывается,
следующим образом:
"""
file = open("work_with_files/users.txt", 'r', encoding='utf-8')
try:
    s = file.readlines()
    print(s)
    int(s)
    print(s)
    file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)
    file.close()
    print(file.closed)



