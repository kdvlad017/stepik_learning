class User:

    def __init__(self, first_name, last_name, national, discount=0, login_attempts=0):
        self.last_name = last_name
        self.first_name = first_name
        self.national = national
        self.discount = discount
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.national} {self.discount} {self.login_attempts}")

    def greet_user(self):
        print(f"Welcome, mr(s) {self.first_name} {self.last_name}")


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = ['разрешено добавлять сообщения',
     'разрешено удалять пользователей',
     'разрешено банить пользователей'
     ]

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, national):
        super().__init__(first_name, last_name, national, discount=0, login_attempts=0)
        self.privileges = Privileges()


restaurant = Restaurant('Rivera', 'European')
user = User('Dmitrii', 'Kalinkin', 'Russian')
ice = IceCreamStand('Morozko', 'Fastfood')
ice.flavors.append('Vanilla')
ice.flavors.append('Chocolate')

admin = Admin('Dmitrii', 'Kalinkin', 'Russian')
admin.privileges.show_privileges()

