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


# # # Exercise

# # 01. Logged
# def logged(func_ref):
#     def wrapper(*args):
#         result = func_ref(*args)
#         return f'you called {func_ref.__name__}{args}\nit returned {result}'
#
#     return wrapper
#
#
# @logged
# def function(*args):
#     return 3 + len(args)


# # 02. Even Parameters
# def even_parameters(func_ref):
#     def wrapper(*args):
#         for argument in args:
#             if not isinstance(argument, int) or argument % 2 != 0:
#                 return 'Please use only even numbers!'
#         return func_ref(*args)
#
#     return wrapper
#
#
# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add('Peter', 1))


# # 03. Bold, Italic, Underline
# def make_bold(func_ref):
#     def wrapper(*args):
#         return f'<b>{func_ref(*args)}</b>'
#
#     return wrapper
#
#
# def make_italic(func_ref):
#     def wrapper(*args):
#         return f'<i>{func_ref(*args)}</i>'
#
#     return wrapper
#
#
# def make_underline(func_ref):
#     def wrapper(*args):
#         return f'<u>{func_ref(*args)}</u>'
#
#     return wrapper
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
#
# print(greet("Peter"))


# # 04. Type Check
# def type_check(type):
#     def decorator(func_ref):
#         def wrapper(argument):
#             if not isinstance(argument, type):
#                 return 'Bad Type'
#             return func_ref(argument)
#
#         return wrapper
#
#     return decorator
#
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# print(times2('Not A Number'))


# # 05. Cache
# def cache(func):
#     def wrapper(num):
#         if not wrapper.log.get(num):
#             wrapper.log[num] = func(num)
#         return wrapper.log[num]
#
#     wrapper.log = {}
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# # 06. HTML Tags
# def tags(tag):
#     def decorator(func_ref):
#         def wrapper(*args):
#             return f'<{tag}>{func_ref(*args)}</{tag}>'
#
#         return wrapper
#
#     return decorator
#
#
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
#
#
# print(join_strings("Hello", " you!"))


# # 07. *Store Results
# class store_results:
#     _FILE_NAME = 'results.txt'
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         with open(store_results._FILE_NAME, 'a') as result_file:
#             result_file.write(f'Function {self.func.__name__} was called. Result: {self.func(*args)}\n')
#
#
# @store_results
# def add(a, b):
#     return a + b
#
#
# @store_results
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)
