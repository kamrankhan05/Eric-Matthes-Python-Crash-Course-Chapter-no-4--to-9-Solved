#
#    ###6-1. Person
# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30,
#     'city': 'New York'
# }
#
# print(f"First Name: {person['first_name']}")
# print(f"Last Name: {person['last_name']}")
# print(f"Age: {person['age']}")
# print(f"City: {person['city']}")
#
#
#    ####    6-2. Favorite Numbers
# favorite_numbers = {
#     'alice': 7,
#     'bob': 42,
#     'charlie': 3,
#     'dave': 8,
#     'eve': 13
# }
#
# for name, number in favorite_numbers.items():
#     print(f"{name.title()}'s favorite number is {number}.")
#
#
#   #### 6-3. Glossary
# glossary = {
#     'variable': 'A named storage location in memory.',
#     'function': 'A reusable block of code.',
#     'loop': 'A structure that repeats a block of code.',
#     'list': 'An ordered collection of items.',
#     'dictionary': 'A collection of key-value pairs.'
# }
#
# for term, definition in glossary.items():
#     print(f"\n{term.title()}:")
#     print(f"\t{definition}")
#
#
#
#     ###6-4. Glossary 2
#
# glossary = {
#     'variable': 'A named storage location in memory.',
#     'function': 'A reusable block of code.',
#     'loop': 'A structure that repeats a block of code.',
#     'list': 'An ordered collection of items.',
#     'dictionary': 'A collection of key-value pairs.',
#     'tuple': 'An immutable list.',
#     'set': 'A collection of unique items.',
#     'string': 'A sequence of characters.',
#     'integer': 'A whole number.',
#     'float': 'A number with a decimal point.'
# }
#
# for term, definition in glossary.items():
#     print(f"\n{term.title()}:")
#     print(f"\t{definition}")
#
#
#     #### 6-5. Rivers
# rivers = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china'
# }
#
# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}.")
#
# print("\nRivers:")
# for river in rivers.keys():
#     print(river.title())
#
# print("\nCountries:")
# for country in rivers.values():
#     print(country.title())
#
#
#          ###6-6. Polling
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# poll_takers = ['jen', 'sarah', 'mike', 'lisa']
#
# for name in poll_takers:
#     if name in favorite_languages:
#         print(f"Thank you, {name.title()}, for taking the poll!")
#     else:
#         print(f"{name.title()}, please take our poll!")
#
#
#         ###    6-7. People
# person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
# person2 = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'Los Angeles'}
# person3 = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 40, 'city': 'Chicago'}
#
# people = [person1, person2, person3]
#
# for person in people:
#     print(f"\nFull Name: {person['first_name']} {person['last_name']}")
#     print(f"Age: {person['age']}")
#     print(f"City: {person['city']}")
#
#
#          ###6-8. Pets
# pet1 = {'animal': 'dog', 'owner': 'alice'}
# pet2 = {'animal': 'cat', 'owner': 'bob'}
# pet3 = {'animal': 'parrot', 'owner': 'charlie'}
#
# pets = [pet1, pet2, pet3]
#
# for pet in pets:
#     print(f"\nAnimal: {pet['animal'].title()}")
#     print(f"Owner: {pet['owner'].title()}")
#
#
#
#     ####    6-9. Favorite Places
# favorite_places = {
#     'alice': ['paris', 'tokyo'],
#     'bob': ['new york'],
#     'charlie': ['berlin', 'rome', 'london']
# }
#
# for name, places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")
#
#
#         ###   6-10. Favorite Numbers (Extended)
# favorite_numbers = {
#     'alice': [7, 11],
#     'bob': [42],
#     'charlie': [3, 9, 27],
#     'dave': [8, 16],
#     'eve': [13, 21, 34]
# }
#
# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\t{number}")
#
#
#
#         ###   6-11. Cities
# cities = {
#     'tokyo': {
#         'country': 'japan',
#         'population': 37_000_000,
#         'fact': 'Hosted the 2020 Olympics.'
#     },
#     'paris': {
#         'country': 'france',
#         'population': 2_100_000,
#         'fact': 'Known as the "City of Light".'
#     },
#     'new york': {
#         'country': 'usa',
#         'population': 8_400_000,
#         'fact': 'Home to the Statue of Liberty.'
#     }
# }
#
# for city, info in cities.items():
#     print(f"\nCity: {city.title()}")
#     print(f"\tCountry: {info['country'].title()}")
#     print(f"\tPopulation: {info['population']}")
#     print(f"\tFact: {info['fact']}")
#
#
#
#
# 
