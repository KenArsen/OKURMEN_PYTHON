"""
open(file [, mode=’r’, encoding=None, …])


file – путь к файлу (вместе с его именем);
mode – режим доступа к файлу (чтение/запись);
encoding – кодировка файла.


При необходимости, мы можем управлять положением файловой позиции.
Для этого существует специальный метод:
file.seek(offset[, from_what])


Если же мы хотим узнать текущую позицию в файле, то следует вызвать метод tell:
pos = file.tell()


Следующий полезный метод readline() позволяет построчно считывать информацию из текстового файла:
s = file.readline()
print(s)

Если нам нужно последовательно прочитать все строчки из файла,
то для этого обычно используют цикл for следующим образом:
for line in file:
    print(line, end="")


Или же, все строчки можно прочитать методом:
s = file.readlines()


Осталось только добавить, что как только мы завершаем работу с файлом, его следует закрыть.
Для этого используется метод close:
file.close()
"""


FILENAME = 'work_with_files/users.txt'

file = open(FILENAME, encoding='utf-8')
print(file.readline(), end='')
print(file.readline(), end='')



for line in file:
    print(line, end='')







