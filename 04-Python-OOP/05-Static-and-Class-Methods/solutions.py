# # # Lab


# # 01. Calculator
# from functools import reduce
#
#
# class Calculator:
#
#     @staticmethod
#     def add(*args):
#         return sum([x for x in args])
#
#     @staticmethod
#     def multiply(*args):
#         return reduce(lambda x, y: x * y, args)
#
#     @staticmethod
#     def divide(*args):
#         return reduce(lambda x, y: x / y, args)
#
#     @staticmethod
#     def subtract(*args):
#         return reduce(lambda x, y: x - y, args)


# # 02. Shop
# class Shop:
#     def __init__(self, name: str, type: str, capacity: int):
#         self.name = name
#         self.type = type
#         self.capacity = capacity
#         self.items = {}
#
#     @classmethod
#     def small_shop(cls, name: str, type: str):
#         return cls(name, type, 10)
#
#     def add_item(self, item_name: str):
#         if sum([x for x in self.items.values()]) < self.capacity:
#             if item_name not in self.items:
#                 self.items[item_name] = 0
#             self.items[item_name] += 1
#             return f'{item_name} added to the shop'
#         return f'Not enough capacity in the shop'
#
#     def remove_item(self, item_name: str, amount: int):
#         if item_name in self.items and amount <= self.items[item_name]:
#             self.items[item_name] -= amount
#             if self.items[item_name] == 0:
#                 del self.items[item_name]
#             return f'{amount} {item_name} removed from the shop'
#         return f'Cannot remove {amount} {item_name}'
#
#     def __repr__(self):
#         return f'{self.name} of type {self.type} with capacity {self.capacity}'


# # 03. Integer
# from math import floor
#
#
# class Integer:
#
#     def __init__(self, value: int):
#         self.value = value
#
#     @classmethod
#     def from_float(cls, float_value):
#         if isinstance(float_value, float):
#             return cls(int(floor(float_value)))
#         return 'value is not a float'
#
#     @classmethod
#     def from_roman(cls, value):
#         roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         result = 0
#         for i, c in enumerate(value):
#             if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
#                 result += roman_numerals[c]
#             else:
#                 result -= roman_numerals[c]
#         return cls(result)
#
#     @classmethod
#     def from_string(cls, value):
#         if isinstance(value, str):
#             return cls(int(value))
#         return 'wrong type'


# # # Exercise

# # 01. Photo Album
# class PhotoAlbum:
#
#     MAX_PHOTOS_ON_PAGE = 4
#     page_separator = f'{"-" * 11}'
#
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = [[] for x in range(self.pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         pages = photos_count // PhotoAlbum.MAX_PHOTOS_ON_PAGE
#         if photos_count % PhotoAlbum.MAX_PHOTOS_ON_PAGE != 0:
#             pages += 1
#         return cls(pages)
#
#     def add_photo(self, label: str):
#         for page in self.photos:
#             if len(page) < self.MAX_PHOTOS_ON_PAGE:
#                 page.append(label)
#                 return f'{label} photo added successfully on page {self.photos.index(page) + 1} slot {page.index(label) + 1}'
#         return 'No more free slots'
#
#     def display(self):
#         my_album = [PhotoAlbum.page_separator]
#         for page in self.photos:
#             if page:
#                 p = ['[]' for _ in page]
#                 my_album.append(' '.join(p))
#                 my_album.append(PhotoAlbum.page_separator)
#             else:
#                 my_album.append('')
#                 my_album.append(PhotoAlbum.page_separator)
#         return '\n'.join(my_album)
