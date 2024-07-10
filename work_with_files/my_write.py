"""
r (Read). Файл открывается для чтения. Если файл не найден,
то генерируется исключение FileNotFoundError


w (Write). Файл открывается для записи. Если файл отсутствует, то он создается.
Если подобный файл уже есть, то он создается заново, и соответственно старые данные в нем стираются.

a (Append). Файл открывается для дозаписи. Если файл отсутствует, то он создается.
Если подобный файл уже есть, то данные записываются в его конец.

b (Binary). Используется для работы с бинарными файлами.
Применяется вместе с другими режимами - w или r, например, rb (чтение бинарных файлов) и wb (запись бинарных файлов).

r+. Файл открывается одновременно для чтения и записи.
Если файл не найден, то генерируется исключение FileNotFoundError

w+. Файл открывается одновременно для чтения и записи.
Если файл не существует, то он автоматически создается. Если файл существует, то он перезаписывается

a+. Файл открывается одновременно для чтения и записи.
Если файл не существует, то он автоматически создается. Если файл существует, то данные добавляются в конец файла
"""

try:
    with open('work_with_files/users_2.txt', 'a') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("File not found")
finally:
    print("Файл успешно прочитан")



