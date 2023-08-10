# # # Lab

# # 01. Number Increment
# def number_increment(numbers):
#
#     def increase():
#         return [x + 1 for x in numbers]
#
#     return increase()

# # 02. Vowel Filter
# from functools import wraps
#
#
# def vowel_filter(function):
#     vowels = 'euyioa'
#
#     @wraps(function)
#     def wrapper():
#         result = function()
#         return [x for x in result if x.lower() in vowels]
#
#     return wrapper
#
#
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]

# print(get_letters())


# # 03. Even Numbers
# from functools import wraps
#
#
# def is_even(x):
#     return x % 2 == 0
#
#
# def even_numbers(function):
#     @wraps(function)
#     def wrapper(numbers):
#         result = function(numbers)
#
#         return [x for x in result if is_even(x)]
#
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))


# # 04. Multiply
# def multiply(times):
#     def decorator(function):
#         def wrapper(params):
#             return times * function(params)
#         return wrapper
#     return decorator