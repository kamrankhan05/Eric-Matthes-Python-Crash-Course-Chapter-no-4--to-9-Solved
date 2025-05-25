

         ####5-1. Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Additional tests
print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs car.lower() == 'SUBARU'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs len(car) > 5? I predict False.")
print(len(car) > 5)



           ###5-2. More Conditional Tests
string1 = 'hello'
string2 = 'world'
print(string1 == string2)  # False
print(string1 != string2)  # True

print(string1.lower() == 'HELLO'.lower())  # True

num1, num2 = 10, 20
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # False
print(num1 <= num2)  # True

print((num1 > 5) and (num2 < 30))  # True
print((num1 > 15) or (num2 < 15))  # False

fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)
print('grape' not in fruits)



          ####5-3. Alien Colors #1
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")



     ###5-4. Alien Colors #2
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")



######  5-5. Alien Colors #3

alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")



      ###5-6. Stages of Life
age = 25
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")



       ####5-7. Favorite Fruit
favorite_fruits = ['banana', 'apple', 'mango']
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")



                ###5-8. Hello Admin
usernames = ['admin', 'eric', 'john', 'jane', 'alice']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")



########  5-9. No Users
usernames = []
if usernames:
    for username in usernames:
        print(f"Hello {username}!")
else:
    print("We need to find some users!")


         ###5-10. Checking Usernames
current_users = ['John', 'Alice', 'Bob', 'Charlie', 'David']
new_users = ['Alice', 'Eric', 'john', 'Frank', 'Grace']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Username '{user}' is taken. Please choose another.")
    else:
        print(f"Username '{user}' is available.")



         ## 5-11. Ordinal Numbers
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")




