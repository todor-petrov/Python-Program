# # # Lab


# # 01. Person
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age


# # 02. Mammal
#
# class Mammal:
#
#     __kingdom = 'animals'
#
#     def __init__(self, name, type, sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#
#     def make_sound(self):
#         return f'{self.name} makes {self.sound}'
#
#     def get_kingdom(self):
#         return f'{self.__kingdom}'
#
#     def info(self):
#         return f'{self.name} is of type {self.type}'


# # 03. Profile
#
# class Profile:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, value):
#         if not 5 <= len(value) <= 15:
#             raise ValueError('The username must be between 5 and 15 characters.')
#         self.__username = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         if not 8 <= len(value) or \
#                 not any(char.isupper() for char in value) or \
#                 not any(char.isdigit() for char in value):
#             raise ValueError('The password must be 8 or more characters with '
#                              'at least 1 digit and 1 uppercase letter.')
#         self.__password = value
#
#     def __str__(self):
#         return (f'You have a profile with username: '
#                 f'"{self.username}" and password: {"*" * len(self.password)}')


# # 04. Email Validator
#
# class EmailValidator:
#
#     def __init__(self, min_length, mails, domains):
#         self.min_length = min_length
#         self.mails = mails
#         self.domains = domains
#
#     def __is_name_valid(self, name):
#         return len(name) >= self.min_length
#
#     def __is_mail_valid(self, mail):
#         return mail in self.mails
#
#     def __is_domain_valid(self, domain):
#         return domain in self.domains
#
#     def validate(self, email):
#         name = email.split('@')[0]
#         mail, domain = email.split('@')[1].split('.')
#         return (self.__is_name_valid(name)
#                 and self.__is_mail_valid(mail)
#                 and self.__is_domain_valid(domain))


# # 05. Account
#
# class Account:
#
#     def __init__(self, id, balance, pin):
#         self.__id = id
#         self.balance = balance
#         self.__pin = pin
#
#     def get_id(self, pin):
#         if not self.__pin == pin:
#             return 'Wrong pin'
#         return self.__id
#
#     def change_pin(self, old_pin, new_pin):
#         if old_pin == self.__pin:
#             self.__pin = new_pin
#             return 'Pin changed'
#         return 'Wrong pin'
