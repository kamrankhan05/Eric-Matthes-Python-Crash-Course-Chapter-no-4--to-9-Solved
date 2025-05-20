### 9-1. Restaurant

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant('The Great Feast', 'Italian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()



###  9-2. Three Restaurants
restaurant1 = Restaurant('Burger King', 'Fast Food')
restaurant2 = Restaurant('Olive Garden', 'Italian')
restaurant3 = Restaurant('Sushi Palace', 'Japanese')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


### 9-3. Users
class User:

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


user1 = User('John', 'Doe', 30, 'New York')
user2 = User('Jane', 'Smith', 25, 'London')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


###   9-4. Number Served
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Pizza Hut', 'Italian')

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 50
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(75)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Customers served: {restaurant.number_served}")



     ### 9-5. Login Attempts
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('John', 'Doe')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")



    #### 9-6. Ice Cream Stand
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        print("\nAvailable flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand('Scoops')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()


      ###  9-7. Admin
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('Admin', 'User')
admin.describe_user()
admin.show_privileges()



   ###  9-8. Privileges
class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name):
        """Initialize admin attributes."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin = Admin('Admin', 'User')
admin.privileges.show_privileges()



    ### 9-9. Battery Upgrade
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)

my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()



   ###  9-10. Imported Restaurant
class Restaurant:
    """A restaurant model."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

from restaurant import Restaurant

restaurant = Restaurant('Pizza Palace', 'Italian')
restaurant.describe_restaurant()



   ##  9-11. Imported Admin
# user_privileges.py
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
from user_privileges import Admin

admin = Admin('Admin', 'User')
admin.privileges.show_privileges()



 ###  9-12. Multiple Modules
# user.py
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


from user import User


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

from admin import Admin

admin = Admin('Admin', 'User')
admin.privileges.show_privileges()




    #####  9-13. Dice
from random import randint


class Die:
    """A simple die model."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(d6.roll_die(), end=' ')
print()

d10 = Die(10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(d10.roll_die(), end=' ')
print()

d20 = Die(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(d20.roll_die(), end=' ')
print()



   ###  9-14. Lottery
from random import choice

# Create a list of numbers and letters
tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
for _ in range(4):
    item = choice(tickets)
    winning_ticket.append(item)

print("Any ticket matching these numbers or letters wins a prize:")
print(winning_ticket)



   ### 9-15. Lottery Analysis
from random import choice

def get_winning_ticket(tickets):
    """Return a winning ticket."""
    winning_ticket = []
    for _ in range(4):
        item = choice(tickets)
        winning_ticket.append(item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Check if all elements match."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 'a', 5, 'b']

attempts = 0
won = False

while not won:
    attempts += 1
    winning_ticket = get_winning_ticket(tickets)
    won = check_ticket(my_ticket, winning_ticket)

print(f"It took {attempts} attempts to win with ticket: {my_ticket}")





