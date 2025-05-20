#     ###  8-1. Message
#
# def display_message():
#     """Prints what I'm learning about in this chapter."""
#     print("I'm learning about functions in this chapter!")
#
# display_message()
#
#
#   ####   8-2. Favorite Book
# def favorite_book(title):
#     """Prints a message about a favorite book."""
#     print(f"One of my favorite books is {title.title()}.")
#
# favorite_book('alice in wonderland')
#
#
#    ###  8-3. T-Shirt (Positional & Keyword Arguments)
# def make_shirt(size, message):
#     """Prints a summary of the shirt."""
#     print(f"Shirt size: {size.upper()}, Message: '{message}'")
#
# make_shirt('medium', 'Python Rocks!')
#
# make_shirt(size='large', message='I love coding')
#
#
#
#    ###  8-4. Large Shirts (Default Parameters)
# def make_shirt(size='large', message='I love Python'):
#     print(f"Shirt size: {size.upper()}, Message: '{message}'")
#
# make_shirt()
#
# make_shirt('medium')
#
# make_shirt('small', 'Keep Calm and Code On')
#
#
#
#     ###   8-5. Cities (Default Country)
# def describe_city(city, country='iceland'):
#     print(f"{city.title()} is in {country.title()}.")
#
# describe_city('reykjavik')
# describe_city('akureyri')
# describe_city('paris', 'france')
#
#
#
#    ###  8-6. City Names (Returning Strings)
# def city_country(city, country):
#     return f"{city.title()}, {country.title()}"
#
# print(city_country('santiago', 'chile'))
# print(city_country('tokyo', 'japan'))
# print(city_country('berlin', 'germany'))
#
#
#
#    ###   8-7. Album (Dictionary Return)
# def make_album(artist, title, songs=None):
#     album = {'artist': artist, 'title': title}
#     if songs:
#         album['songs'] = songs
#     return album
#
# print(make_album('pink floyd', 'dark side of the moon'))
# print(make_album('radiohead', 'ok computer'))
# print(make_album('the beatles', 'abbey road', songs=17))
#
#
#
#    ###   8-8. User Albums (While Loop)
#
# def make_album(artist, title):
#      return {'artist': artist, 'title': title}
#
#
# while True:
#         print("\nEnter album details (or 'q' to quit):")
#         artist = input("Artist: ")
#         if artist == 'q':
#             break
#         title = input("Title: ")
#         if title == 'q':
#             break
#
#         album = make_album(artist, title)
#         print(f"Album created: {album}")
#
#
#
#
#    ###   8-9. Messages (List Processing)
# def show_messages(messages):
#     for message in messages:
#         print(message)
#
# messages = ['Hello!', 'How are you?', 'Python is fun!']
# show_messages(messages)
#
#
#
#   ###  8-10. Sending Messages (Moving Items Between Lists)
# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop(0)
#         print(f"Sending: {current_message}")
#         sent_messages.append(current_message)
#
# messages = ['Hello!', 'How are you?', 'Python is fun!']
# sent_messages = []
#
# send_messages(messages, sent_messages)
# print("\nOriginal messages:", messages)
# print("Sent messages:", sent_messages)
#
#
# 
#       ###8-11. Archived Messages (List Copy)
# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop(0)
#         print(f"Sending: {current_message}")
#         sent_messages.append(current_message)
#
# messages = ['Hello!', 'How are you?', 'Python is fun!']
# sent_messages = []
#
# send_messages(messages[:], sent_messages)
# print("\nOriginal messages:", messages)
# print("Sent messages:", sent_messages)
#
#
#
#      ###  8-12. Sandwiches (Arbitrary Arguments)
# def make_sandwich(*items):
#     print("\nMaking a sandwich with:")
#     for item in items:
#         print(f"- {item}")
#
# make_sandwich('ham', 'cheese')
# make_sandwich('turkey', 'lettuce', 'tomato')
# make_sandwich('peanut butter', 'jelly')
#
#
#
#     ###  8-13. User Profile (Dictionary with Arbitrary Keyword Arguments)
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# my_profile = build_profile('john', 'doe',
#                           age=30,
#                           occupation='developer',
#                           hobby='gaming')
# print(my_profile)
#
#
#
#     ##   8-14. Cars (Dictionary with Required and Optional Arguments)
# def make_car(manufacturer, model, **car_info):
#     car_info['manufacturer'] = manufacturer
#     car_info['model'] = model
#     return car_info
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)
#
#
#
#    ####   8-15. Printing Models (Module Import)
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print("\nCompleted models:")
#     for model in completed_models:
#         print(model)
#
# import printing_functions
#
# unprinted = ['phone case', 'robot pendant', 'dodecahedron']
# completed = []
#
# printing_functions.print_models(unprinted, completed)
# printing_functions.show_completed_models(completed)
#
#
#
#      ### 8-16. Imports (Different Import Styles)
# # my_module.py
# def greet(name):
#
#     print(f"Hello, {name}!")
#
# import my_module
# my_module.greet('Alice')
#
# from my_module import greet
# greet('Bob')
#
# from my_module import greet as g
# g('Charlie')
#
# import my_module as mm
# mm.greet('David')
#
# from my_module import *
# greet('Eve')