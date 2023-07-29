# # # Lab

# # 01. Rhombus of Stars
# number, rhombus = int(input()), []
# for i in range(1, number + 1):
#     rhombus.append(' ' * (number - i) + ' '.join('*' * i))
# rhombus.extend(rhombus[:-1][::-1])
# print('\n'.join(rhombus))


# # 02. Scope Mess
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         global x
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
#
# print(x)
# outer()
# print(x)


# # 03. Class Book
# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages


# # 04. Car
# class Car:
#     def __init__(self, name, model, engine):
#         self.name = name
#         self.model = model
#         self.engine = engine
#
#     def get_info(self):
#         return f'This is {self.name} {self.model} with engine {self.engine}'


# # 05. Music
# class Music:
#     def __init__(self, title, artist, lyrics):
#         self.title = title
#         self.artist = artist
#         self.lyrics = lyrics
#
#     def print_info(self):
#         return f'This is "{self.title}" from "{self.artist}"'
#
#     def play(self):
#         return f'{self.lyrics}'


# # # Exercise

# # 01. Shop
# class Shop:
#     def __init__(self, name, items):
#         self.name = name
#         self.items = items
#
#     def get_items_count(self):
#         return len(self.items)


# # 02. Hero
# class Hero:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def defend(self, damage):
#         self.health -= damage
#         if self.health <= 0:
#             self.health = 0
#             return f'{self.name} was defeated'
#
#     def heal(self, amount):
#         self.health += amount


# # 03. Employee
# class Employee:
#     def __init__(self, id, first_name, last_name, salary):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def get_annual_salary(self):
#         return self.salary * 12
#
#     def raise_salary(self, amount):
#         self.salary += amount
#         return self.salary


# # 04. Cup
# class Cup:
#     def __init__(self, size, quantity):
#         self.size = size
#         self.quantity = quantity
#
#     def fill(self, quantity):
#         if self.quantity + quantity <= self.size:
#             self.quantity += quantity
#
#     def status(self):
#         return self.size - self.quantity


# # 05. Flower
# class Flower:
#     def __init__(self, name, water_requirements):
#         self.name = name
#         self.water_requirements = water_requirements
#         self.is_happy = False
#
#     def water(self, quantity):
#         if self.water_requirements <= quantity:
#             self.is_happy = True
#
#     def status(self):
#         return f'{self.name} is happy' if self.is_happy else f'{self.name} is not happy'


# # 06. Steam User
# class SteamUser:
#     def __init__(self, username, games):
#         self.username = username
#         self.games = games
#         self.played_hours = 0
#
#     def play(self, game, hours):
#         if game not in self.games:
#             return f'{game} is not in library'
#         self.played_hours += hours
#         return f'{self.username} is playing {game}'
#
#     def buy_game(self, game):
#         if game not in self.games:
#             self.games.append(game)
#             return f'{self.username} bought {game}'
#         return f'{game} is already in your library'
#
#     def status(self):
#         return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


# # 07. Programmer
# class Programmer:
#     def __init__(self, name, language, skills):
#         self.name = name
#         self.language = language
#         self.skills = skills
#
#     def watch_course(self, course_name, language, skills_earned):
#         if not self.language == language:
#             return f'{self.name} does not know {language}'
#         self.skills += skills_earned
#         return f'{self.name} watched {course_name}'
#
#     def change_language(self, new_language, skills_needed):
#         if self.skills >= skills_needed and new_language != self.language:
#             previous_language = self.language
#             self.language = new_language
#             return f'{self.name} switched from {previous_language} to {new_language}'
#         elif self.skills >= skills_needed and new_language == self.language:
#             return f'{self.name} already knows {self.language}'
#         elif self.skills < skills_needed:
#             needed_skills = skills_needed - self.skills
#             return f'{self.name} needs {needed_skills} more skills'