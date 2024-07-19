class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, salary)
        Student.__init__(self, name, age)


workingStudent = WorkingStudent('Jack', 25, 10000)
workingStudent.display()
print(WorkingStudent.__mro__)
print(WorkingStudent.mro())

