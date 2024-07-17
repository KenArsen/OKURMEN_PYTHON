# def say_name(name):
#     def say_goodbay():
#         print(f"Don't say me goodbay, {name}!")
    
#     def say_hello():
#         print(f"Hello, {name}")
    
#     say_goodbay()
#     say_hello()

# say_name("Arsen")

def say_name(name):
    def say_goodbay():
        print(f"Don't say me goodbay, {name}!")
    
    return say_goodbay

a = say_name("Arsen")
a()


def get_book(name):
    def get_author(author):
        print(f"The book {name} - author {author}")
    
    return get_author

a = get_book("Harry Potter")
a("J.K.Rowling")

def make_counter(n = 0):
    def next():
        nonlocal n
        n += 1
        return n
    return next

t_1 = make_counter()
t_2 = make_counter(10)
print(t_1(), t_2())
print(t_1(), t_2())
print(t_1(), t_2())



def limited_calls(func_1, n):
    def limit():
        nonlocal n
        n -= 1
        if n < 0:
            print("Limit reached")
        else:
            func_1()
    return limit

def func():
    print("Function was called")


a = limited_calls(func_1=func, n=5)
a()
a()
a()
a()
a()
a()
a()
a()