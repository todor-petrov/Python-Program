# # # Lab

# # 01. Vehicle
# class Vehicle:
#     def __init__(self, mileage, max_speed=150):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets = []


# # 02. Point
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f'The point has coordinates ({self.x},{self.y})'


# # 03. Circle
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         return Circle.pi * (self.radius ** 2)
#
#     def get_circumference(self):
#         return 2 * Circle.pi * self.radius


# # 04. Glass
# class Glass:
#
#     MAX_CAPACITY = 250
#     capacity = MAX_CAPACITY
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if self.content + ml > self.capacity:
#             return f'Cannot add {ml} ml'
#         self.content += ml
#         return f'Glass filled with {ml} ml'
#
#     def empty(self):
#         self.content = 0
#         return f'Glass is now empty'
#
#     def info(self):
#         return f'{self.capacity - self.content} ml left'


# # 05. Smartphone
# class Smartphone:
#
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         self.is_on = True
#
#     def install(self, app, app_memory):
#         if app_memory <= self.memory and self.is_on:
#             self.memory -= app_memory
#             self.apps.append(app)
#             return f'Installing {app}'
#         if app_memory <= self.memory and not self.is_on:
#             return f'Turn on your phone to install {app}'
#         return f'Not enough memory to install {app}'
#
#     def status(self):
#         return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


# # # Exercise

# # 01. Vet
# class Vet:
#
#     animals = []
#     space = 5
#
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if Vet.space == 0:
#             return f'Not enough space'
#         Vet.animals.append(animal_name)
#         self.animals.append(animal_name)
#         Vet.space -= 1
#         return f'{animal_name} registered in the clinic'
#
#     def unregister_animal(self, animal_name):
#         if animal_name not in Vet.animals:
#             return f'{animal_name} not in the clinic'
#         Vet.animals.remove(animal_name)
#         Vet.space += 1
#         self.animals.remove(animal_name)
#         return f'{animal_name} unregistered successfully'
#
#     def info(self):
#         return f'{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic'


# # 02. Time
# class Time:
#
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
#
#     def next_second(self):
#         self.seconds += 1
#         if self.seconds == 60:
#             self.seconds = 0
#             self.minutes += 1
#         if self.minutes == 60:
#             self.minutes = 0
#             self.hours += 1
#         if self.hours == 24:
#             self.hours = 0
#         return self.get_time()


# # 03. Account
# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount > self.balance:
#             return f'Amount exceeded balance'
#         self.balance -= amount
#         return self.balance
#
#     def info(self):
#         return f'User {self.name} with account {self.id} has {self.balance} balance'


# # 04. Pizza Delivery
# class PizzaDelivery:
#
#     def __init__(self, name: str, price: int, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = 0
#         self.ingredients[ingredient] += quantity
#         self.price += (price_per_quantity * quantity)
#
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
#         if ingredient in self.ingredients and quantity <= self.ingredients[ingredient]:
#             self.price -= (price_per_quantity * quantity)
#             self.ingredients[ingredient] -= quantity
#         return f'Please check again the desired quantity of {ingredient}!'
#
#     def make_order(self):
#         self.ordered = True
#         pizza = []
#         for i, q in self.ingredients.items():
#             pizza.append(f'{i}: {q}')
#         return f"You've ordered pizza {self.name} prepared with {', '.join(pizza)} and the price will be {self.price}lv."
