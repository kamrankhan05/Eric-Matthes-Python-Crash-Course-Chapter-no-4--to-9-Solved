#                                          CHAPTER : NO 11

#def get_formatted_name(first_name, last_name):
#
#     full_name = f"{first_name.title()} {last_name.title()}"
#     return full_name
#
# import unittest
# from name_function import get_formatted_name
#
# class NamesTestCase(unittest.TestCase):
#     """Tests for get_formatted_name()."""
#
#     def test_first_last_name(self):
#         """Do names like 'janis joplin' work?"""
#         formatted = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted, 'Janis Joplin')
#
# if _name_ == '_main_':
#     unittest.main()



# def get_formatted_name(first_name, last_name, middle_name=''):
#
#     if middle_name:
#         full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
#     else:
#         full_name = f"{first_name.title()} {last_name.title()}"
#     return full_name



# def make_album(artist, title, tracks=None):
#
#     album = {'artist': artist.title(), 'title': title.title()}
#     if tracks is not None:
#         album['tracks'] = tracks
#     return album




# import unittest
# from name_function import get_formatted_name
# from album_function import make_album
#
# class NamesTestCase(unittest.TestCase):
#     """Tests for get_formatted_name()."""
#
#     def test_first_last_name(self):
#         """Do names like 'janis joplin' work?"""
#         formatted = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted, 'Janis Joplin')
#
#     def test_first_middle_last_name(self):
#         """Do names like 'john lee hooker' work?"""
#         formatted = get_formatted_name('john', 'hooker', 'lee')
#         self.assertEqual(formatted, 'John Lee Hooker')
#
# class AlbumTestCase(unittest.TestCase):
#     """Tests for make_album()."""
#
#     def test_make_album_without_tracks(self):
#         """Can we make an album dict without tracks?"""
#         album = make_album('pink floyd', 'the wall')
#         expected = {'artist': 'Pink Floyd', 'title': 'The Wall'}
#         self.assertEqual(album, expected)
#
#     def test_make_album_with_tracks(self):
#         """Can we make an album dict with a track count?"""
#         album = make_album('metallica', 'ride the lightning', tracks=8)
#         expected = {
#             'artist': 'Metallica',
#             'title': 'Ride The Lightning',
#             'tracks': 8
#         }
#         self.assertEqual(album, expected)
#
# if _name_ == '_main_':
#     unittest.main()





#
# def verify_user(username, active_users):
#
#     username_lower = username.lower()
#     active_lower = [user.lower() for user in active_users]
#     return username_lower in active_lower



#
# import unittest
# from user_functions import verify_user
#
# class VerifyUserTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.active_users = ['alice', 'bob', 'charlie']
#
#     def test_user_found_exact_case(self):
#         result = verify_user('alice', self.active_users)
#         self.assertTrue(result)
#
#     def test_user_found_different_case(self):
#         result = verify_user('Alice', self.active_users)
#         self.assertTrue(result)
#
#     def test_user_not_found(self):
#         result = verify_user('david', self.active_users)
#         self.assertFalse(result)
#
# if _name_ == '_main_':
#     unittest.main()





# class Restaurant:
#
#     def _init_(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name.title()
#         self.cuisine_type = cuisine_type.lower()
#         self.number_served = 0
#
#     def set_number_served(self, number):
#
#         if number >= 0:
#             self.number_served = number
#         else:
#             raise ValueError("Number served cannot be negative.")
#
#     def increment_number_served(self, additional):
#         if additional >= 0:
#             self.number_served += additional
#         else:
#             raise ValueError("Increment must be non-negative.")



# import unittest
# from restaurant import Restaurant
#
# class RestaurantTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.restaurant = Restaurant('Pasta Palace', 'Italian')
#
#     def test_default_number_served(self):
#         self.assertEqual(self.restaurant.number_served, 0)
#
#     def test_set_number_served(self):
#         self.restaurant.set_number_served(30)
#         self.assertEqual(self.restaurant.number_served, 30)
#
#     def test_increment_number_served(self):
#         self.restaurant.set_number_served(30)
#         self.restaurant.increment_number_served(15)
#         self.assertEqual(self.restaurant.number_served, 45)
#
#     def test_set_number_negative_raises(self):
#         with self.assertRaises(ValueError):
#             self.restaurant.set_number_served(-5)
#
#     def test_increment_negative_raises(self):
#         with self.assertRaises(ValueError):
#             self.restaurant.increment_number_served(-10)
#
# if _name_ == '_main_':
#     unittest.main()





# def city_country(city, country, population=None):
#
#     if population:
#         return f"{city.title()}, {country.title()} – population {population:,}"
#     else:
#         return f"{city.title()}, {country.title()}"




# import unittest
# from city_functions import city_country
#
# class CityCountryTestCase(unittest.TestCase):
#
#     def test_city_country_without_population(self):
#         result = city_country('santiago', 'chile')
#         self.assertEqual(result, 'Santiago, Chile')
#
#     def test_city_country_with_population(self):
#
#         result = city_country('santiago', 'chile', population=5000000)
#         self.assertEqual(result, 'Santiago, Chile – population 5,000,000')
#
# if _name_ == '_main_':
#     unittest.main()





# class Die:
#     """A simple model of a die."""
#
#     def _init_(self, num_sides=6):
#         self.num_sides = num_sides
#
#     def roll_die(self):
#         """Return a random value between 1 and num_sides."""
#         from random import randint
#         return randint(1, self.num_sides)





# import random
#
# class Die:
#
#     def _init_(self, num_sides=6):
#         self.num_sides = num_sides
#
#     def roll_die(self):
#
#         return random.randint(1, self.num_sides)




# import unittest
# from die import Die
#
# class DieTestCase(unittest.TestCase):
#
#     def test_roll_die_within_range(self):
#         die = Die()  # Default 6-sided
#         roll = die.roll_die()
#         self.assertIn(roll, range(1, die.num_sides + 1),
#                       "roll_die() returned a value outside 1–6")
#
#     def test_roll_die_all_values(self):
#         die = Die()
#         results = [die.roll_die() for _ in range(100)]
#         for side in range(1, die.num_sides + 1):
#             self.assertIn(side, results,
#                           f"Value {side} did not appear in 100 rolls")
#
#     def test_custom_sided_die(self):
#         die = Die(num_sides=10)
#         roll = die.roll_die()
#         self.assertIn(roll, range(1, 11),
#                       "roll_die() returned a value outside 1–10 for a 10-sided die")
#
# if _name_ == '_main_':
#     unittest.main()




