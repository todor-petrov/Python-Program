# # # Lab

# # 02. Image Area
# class ImageArea:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def __gt__(self, other):
#         return self.get_area() > other.get_area()
#
#     def __ge__(self, other):
#         return self.get_area() >= other.get_area()
#
#     def __lt__(self, other):
#         return self.get_area() < other.get_area()
#
#     def __le__(self, other):
#         return self.get_area() <= other.get_area()
#
#     def __eq__(self, other):
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):
#         return self.get_area() != other.get_area()


# # 03. Playing
#
# def start_playing(instance):
#     return instance.play()


# # 04. Shapes
# from abc import ABC, abstractmethod
# from math import pi
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def calculate_area(self):
#         return pi * self.__radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * pi * self.__radius
#
#
# class Rectangle(Shape):
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#
#     def calculate_area(self):
#         return self.__width * self.__height
#
#     def calculate_perimeter(self):
#         return (self.__height + self.__width) * 2


# # # Exercise

# # 01. Vehicle
# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     def __init__(self, fuel_quantity, fuel_consumption):
#         self.fuel_quantity = fuel_quantity
#         self.fuel_consumption = fuel_consumption
#
#     @abstractmethod
#     def drive(self, distance):
#         pass
#
#     @abstractmethod
#     def refuel(self, fuel):
#         pass
#
#
# class Car(Vehicle, ABC):
#     def __init__(self, fuel_quantity, fuel_consumption):
#         super().__init__(fuel_quantity, fuel_consumption)
#
#     def drive(self, distance):
#         needed_fuel = distance * (self.fuel_consumption + 0.9)
#         if needed_fuel <= self.fuel_quantity:
#             self.fuel_quantity -= needed_fuel
#             return self.fuel_quantity
#
#     def refuel(self, fuel):
#         self.fuel_quantity += fuel
#
#
# class Truck(Vehicle, ABC):
#
#     def __init__(self, fuel_quantity, fuel_consumption):
#         super().__init__(fuel_quantity, fuel_consumption)
#
#     def drive(self, distance):
#         needed_fuel = distance * (self.fuel_consumption + 1.6)
#         if needed_fuel <= self.fuel_quantity:
#             self.fuel_quantity -= needed_fuel
#             return self.fuel_quantity
#
#     def refuel(self, fuel):
#         self.fuel_quantity += 0.95 * fuel


# # 02. Groups
#
# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'
#
#     def __add__(self, other):
#         return f'{self.name} {other.surname}'
#
#
# class Group:
#
#     def __init__(self, name: str, people: list):
#         self.name = name
#         self.people = people
#
#     def __len__(self):
#         return len(self.people)
#
#     def __add__(self, other):
#         new_name = f'{self.name} {other.name}'
#         members = self.people + other.people
#         return Group(new_name, members)
#
#     def __str__(self):
#         return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"
#
#     def __getitem__(self, index):
#         return f'Person {index}: {self.people[index]}'


# # 03. Accounts
# class Account:
#     def __init__(self, owner, amount=0):
#         self.owner = owner
#         self.amount = amount
#         self._transactions = []
#
#     @property
#     def balance(self):
#         return sum(self._transactions) + self.amount
#
#     def handle_transaction(self, transaction_amount):
#         if self.balance + transaction_amount < 0:
#             raise ValueError("sorry cannot go in debt!")
#
#         self._transactions.append(transaction_amount)
#
#         return f"New balance: {self.balance}"
#
#     def add_transaction(self, amount):
#         if not isinstance(amount, int):
#             raise ValueError("please use int for amount")
#
#         return self.handle_transaction(amount)
#
#     def __str__(self):
#         return f"Account of {self.owner} with starting amount: {self.amount}"
#
#     def __repr__(self):
#         return f"Account({self.owner}, {self.amount})"
#
#     def __len__(self):
#         return len(self._transactions)
#
#     def __getitem__(self, idx):
#         return self._transactions[idx]
#
#     def __reversed__(self):
#         return reversed(self._transactions)
#
#     def __gt__(self, other):
#         return self.balance > other.balance
#
#     def __ge__(self, other):
#         return self.balance >= other.balance
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __add__(self, other):
#         new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
#         new_account._transactions = self._transactions + other._transactions
#         return new_account
