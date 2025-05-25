#   ###  7-1. Rental Car
# car = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a {car.title()}.")
#
#
#
#    ###  7-2. Restaurant Seating
# party_size = input("How many people are in your dinner group? ")
# party_size = int(party_size)
#
# if party_size > 8:
#     print("You'll have to wait for a table.")
# else:
#     print("Your table is ready.")
#
#
#
#        ####  7-3. Multiples of Ten
# number = input("Enter a number: ")
# number = int(number)
#
# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is not a multiple of 10.")
#
#
#
#   #####    7-4. Pizza Toppings (Conditional Test)
# prompt = "\nEnter a pizza topping:"
# prompt += "\n(Enter 'quit' to finish.) "
#
# topping = ""
# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"Adding {topping} to your pizza!")
#
#
#
#         ###   7-4. Pizza Toppings (Active Variable)
#
# prompt = "\nEnter a pizza topping:"
# prompt += "\n(Enter 'quit' to finish.) "
#
# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"Adding {topping} to your pizza!")
#
#
#
#         ###  7-4. Pizza Toppings (Break Statement)
# prompt = "\nEnter a pizza topping:"
# prompt += "\n(Enter 'quit' to finish.) "
#
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"Adding {topping} to your pizza!")
#
#
#
#     #### 7-5. Movie Tickets (Conditional Test)
# prompt = "\nEnter your age:"
# prompt += "\n(Enter 'quit' to exit.) "
#
# age = ""
# while age != 'quit':
#       age = input(prompt)
#       if age == 'quit':
#           break
#       age = int(age)
#
#       if age < 3:
#           print("Your ticket is free!")
#       elif age <= 12:
#           print("Your ticket costs $10.")
#       else:
#           print("Your ticket costs $15.")
#
#
#         ###  7-5. Movie Tickets (Active Variable)
# prompt = "\nEnter your age:"
# prompt += "\n(Enter 'quit' to exit.) "
#
# active = True
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print("Your ticket is free!")
#         elif age <= 12:
#             print("Your ticket costs $10.")
#         else:
#             print("Your ticket costs $15.")
#
#
#
#         ###   7-5. Movie Tickets (Break Statement)
# prompt = "\nEnter your age:"
# prompt += "\n(Enter 'quit' to exit.) "
#
# while True:
#       age = input(prompt)
#       if age == 'quit':
#           break
#       age = int(age)
#
#       if age < 3:
#           print("Your ticket is free!")
#       elif age <= 12:
#           print("Your ticket costs $10.")
#       else:
#           print("Your ticket costs $15.")
#
#
#     ###   7-7. Infinity
#
# while True:
#     print("This loop will never end! Press Ctrl-C to exit.")
#
#
#       ###  7-8. Deli
# sandwich_orders = ['tuna', 'pastrami', 'club', 'pastrami', 'veggie', 'pastrami']
# finished_sandwiches = []
#
# print("The deli has run out of pastrami!\n")
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I made your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\nFinished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich.title()}")
#
#
#
#    ##  7-10. Dream Vacation
#
# responses = {}
# polling_active = True
# while polling_active:
#       name = input("\nWhat is your name? ")
#       response = input("If you could visit one place in the world, where would you go? ")
#
#       responses[name] = response
#
#       repeat = input("Would you like to let another person respond? (yes/no) ")
#       if repeat == 'no':
#           polling_active = False
#
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#       print(f"{name.title()} would like to visit {response.title()}.")
#
#
