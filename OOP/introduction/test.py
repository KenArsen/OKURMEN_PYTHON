# int, float, bool, str, list, tuple, set, dict
# print(), input(), len(), range()


class Employee:
    first_name = "Arsen"
    last_name = "Kenzhegulov"
    age = 22
    gender = "Male"

    def get_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.gender)
        print()

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender


emp1 = Employee()
emp2 = Employee()

emp1.get_info()
emp1.set_first_name(first_name="Amantur")
emp1.get_info()









