from my_functions import set_number, check, start, set_range

def main():
    while True:
        print(f'1. start')
        print(f'2. set range')
        data = int(input("Выберите одну команду: "))

        if data == 1: 
            start()
        elif data == 2:
            start(is_range=True)
        
if __name__ == "__main__":
    main()
        
