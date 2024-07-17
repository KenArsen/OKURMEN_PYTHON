"""
JSON (JavaScript Object Notation) - это текстовый формат для хранения и обмена данными.

Для чтения в модуле json есть два метода:
    json.load - метод считывает файл в формате JSON и возвращает объекты Python
    json.loads - метод считывает строку в формате JSON и возвращает объекты Python

Для записи информации в формате JSON в модуле json также два метода:
    json.dump - метод записывает объект Python в файл в формате JSON
    json.dumps - метод возвращает строку в формате JSON
"""

import json

with open('base_python/work_with_files/sw_templates.json') as f:
    # templates = json.load(f)
    file_content = f.read()
    templates = json.loads(file_content)
print(templates)

for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))
