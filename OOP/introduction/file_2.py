class Person:

    def __init__(self, first_name, last_name, email, password="user_password"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_info(self):
        print(
            self.first_name,
            self.last_name,
            self.email,
            self.password
        )

    def change_password(self, password):
        self.password = password

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __del__(self, ):
        print("Finished")


ob_1 = Person('Ali', 'Turgunbaev', 'ali@gmail.com', "ali_password")
ob_2 = Person('Amantur', 'Nurlanbekuuu', 'amantur@gmail.com', "amantur_password")
ob_1.get_info()
ob_2.get_info()
print(ob_1.get_full_name())
print(ob_2.get_full_name())
