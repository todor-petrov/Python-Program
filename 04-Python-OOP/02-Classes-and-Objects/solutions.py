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
