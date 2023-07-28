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