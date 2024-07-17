try:
    with open("work_with_files/users_1.txt", "r+", encoding="utf-8") as file:
        content = file.read().strip('\n')
        print(content[::-1])
        file.write(content[::-1].strip('\n'))
except FileNotFoundError:
    print("File not found")
