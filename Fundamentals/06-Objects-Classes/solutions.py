# # # Lab

# # 01. Comments
# class Comment:
#     def __init__(self, username: str, content: str, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes

# # 02. Party
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def name_of_attendees(self):
#         return ', '.join([person.name for person in self.people])
#
#     def number_of_guests(self):
#         return len(self.people)
#
#
# party = Party()
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#
#     name = command
#     person = Person(name)
#     party.invite(person)
#
# print(f'Going: {party.name_of_attendees()}')
# print(f'Total: {party.number_of_guests()}')

# # 03. Email
# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
#
# while True:
#     command = input()
#
#     if command == 'Stop':
#         break
#
#     sender, receiver, content = command.split()
#     email = Email(sender, receiver, content)
#     emails.append(email)
#
# send_email = [emails[int(x)].send() for x in input().split(', ')]
#
# for email in emails:
#     print(email.get_info())

# # 04. Zoo
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ''
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}"
#
#         result += f'\nTotal animals: {Zoo.__animals}'
#
#         return result
#
#
# name_of_zoo = input()
# zoo = Zoo(name_of_zoo)
# number_of_lines = int(input())
#
# for _ in range(number_of_lines):
#     info = input().split(' ')
#     species = info[0]
#     type_of_animal = info[1]
#     zoo.add_animal(species, type_of_animal)
#
# additional_info = input()
# print(zoo.get_info(additional_info))

# # 05. Circle
# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return 2 * Circle.__pi * self.radius
#
#     def calculate_area(self):
#         return Circle.__pi * self.radius ** 2
#
#     def calculate_area_of_sector(self, angle):
#         return Circle.__pi * self.radius * self.radius * (angle / 360)
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")


# # # Exercise

# # 01. Storage
# class Storage:
#     storage = []
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def add_product(self, product: str):
#         if len(Storage.storage) < self.capacity:
#             Storage.storage.append(product)
#
#     def get_products(self):
#         return self.storage

# # 02. Weapon
# class Weapon:
#     def __init__(self, bullets: int):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return 'shooting...'
#         return 'no bullets left'
#
#     def __repr__(self):
#         return f'Remaining bullets: {self.bullets}'

# # 03. Catalogue
# class Catalogue:
#     products = []
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def add_product(product_name):
#         Catalogue.products.append(product_name)
#
#     @staticmethod
#     def get_by_letter(first_letter: str):
#         return [x for x in Catalogue.products if first_letter == x[0]]
#
#     def __repr__(self):
#         result = f'Items in the {self.name} catalogue:\n'
#         result += '\n'.join(sorted(Catalogue.products))
#         return result

# # 03. Town
# class Town:
#     def __init__(self, name):
#         self.name = name
#         self.latitude = '0°N'
#         self.longitude = '0°E'
#
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'

# # 04. Class
# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students, self.grades = [], []
#
#     def add_student(self, student_name: str, grade: float):
#         if len(self.students) < Class.__students_count:
#             self.students.append(student_name)
#             self.grades.append(grade)
#
#     def get_average_grade(self):
#         if self.grades:
#             average_grade = float(f'{(sum(self.grades) / len(self.grades)):.2f}')
#             return average_grade
#
#     def __repr__(self):
#         return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"

# # 05. Inventory
# class Inventory:
#     def __init__(self, capacity: int):
#         self.__capacity = capacity
#         self.items = []
#
#     def add_item(self, item: str):
#         if len(self.items) < self.__capacity:
#             self.items.append(item)
#             return
#         return 'not enough room in the inventory'
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         left_capacity = self.__capacity - len(self.items)
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"

# # 07. Articles
# class Article:
#     def __init__(self, title: str, content: str, author: str):
#         self.title = title
#         self.content = content
#         self.author = author
#
#     def edit(self, new_content: str):
#         self.content = new_content
#
#     def change_author(self, new_author: str):
#         self.author = new_author
#
#     def rename(self, new_title: str):
#         self.title = new_title
#
#     def __repr__(self):
#         return f'{self.title} - {self.content}: {self.author}'

# # 08. Vehicle
# class Vehicle:
#     def __init__(self, type, model, price):
#         self.type = type
#         self.model = model
#         self.price = price
#         self.owner = None
#
#     def buy(self, money, owner):
#         if self.owner is None:
#             if money >= self.price:
#                 change = money - self.price
#                 self.owner = owner
#                 return f'Successfully bought a {self.type}. Change: {change:.2f}'
#             else:
#                 return 'Sorry, not enough money'
#         else:
#             return 'Car already sold'
#
#     def sell(self):
#         if self.owner is None:
#             return 'Vehicle has no owner'
#         else:
#             self.owner = None
#
#     def __repr__(self):
#         if self.owner is not None:
#             return f'{self.model} {self.type} is owned by: {self.owner}'
#         else:
#             return f'{self.model} {self.type} is on sale: {self.price}'

# # 09. Movie
# class Movie:
#     __watched_movies = 0
#
#     def __init__(self, name, director):
#         self.name = name
#         self.director = director
#         self.watched = False
#
#     def change_name(self, new_name: str):
#         self.name = new_name
#
#     def change_director(self, new_director: str):
#         self.director = new_director
#
#     def watch(self):
#         if not self.watched:
#             self.watched = True
#             Movie.__watched_movies += 1
#
#     def __repr__(self):
#         return f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}'