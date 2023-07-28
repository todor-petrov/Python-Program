# # # Lab

# # 01. Absolute Values
# def my_func(args):
#     print([abs(float(x)) for x in args])
#
#
# my_func(input().split(' '))

# # 02. Grades
# def grade_func(number):
#     grades = {'Fail': [2.00, 2.99],
#               'Poor': [3.00, 3.49],
#               'Good': [3.50, 4.49],
#               'Very Good': [4.50, 5.49],
#               'Excellent': [5.50, 6.00]}
#     for grade in grades:
#         if grades[grade][0] <= number <= grades[grade][1]:
#             return grade
#
#
# grade_data = float(input())
# print(grade_func(grade_data))

# # 03. Calculations
# operation = input()
# first, second = int(input()), int(input())
#
#
# def my_func(action, n_1, n_2):
#     data = {'multiply': n_1 * n_2,
#             'divide': n_1 / n_2,
#             'add': n_1 + n_2,
#             'subtract': n_1 - n_2}
#     return int(data[action])
#
#
# print(my_func(operation, first, second))

# # 04. Repeat Strinf
# string, number = input(), int(input())
#
#
# def solve(line, count):
#     return line * count
#
#
# print(solve(string, number))

# # 05. Orders
# stock, amount = input(), int(input())
#
#
# def result(product, quantity):
#     products = {'coffee': 1.50, 'water': 1.00, 'coke': 1.40, 'snacks': 2.00}
#     return f'{(products[product] * quantity):.2f}'
#
#
# print(result(stock, amount))

# # 06. Calculate Rectangle Area
# width, height = int(input()), int(input())
#
#
# def area_func(a, h):
#     return a * h
#
#
# print(area_func(width, height))

# # 07. Rounding
# line = [float(x) for x in input().split(' ')]
#
#
# def round_func(data):
#     return [round(x) for x in data]
#
#
# print(round_func(line))


# # # Exercise

# # 01. Smallest of Three Numbers
# one, two, three = int(input()), int(input()), int(input())
#
#
# def return_smallest(a, b, c):
#     return min([a, b, c])
#
#
# print(return_smallest(one, two, three))

# # 02. Add and Subtract
# one, two, three = int(input()), int(input()), int(input())
#
#
# def add_and_subtract(a, b, c):
#     def sum_numbers():
#         return a + b
#
#     def subtract():
#         return sum_numbers() - c
#
#     return subtract()
#
#
# print(add_and_subtract(one, two, three))

# # 03. Characters in Range
# a, b = input(), input()
#
#
# def ascii_generator(x, y):
#     x_ascii, y_ascii = ord(x), ord(y)
#     result = []
#     for i in range(x_ascii + 1, y_ascii):
#         result.append(chr(i))
#     return ' '.join(result)
#
#
# print(ascii_generator(a, b))

# # 04. Odd and Even Sum
# number = input()
#
#
# def even_odd_sum(num):
#     num_list = list(num)
#     even_sum = sum([int(x) for x in num_list if int(x) % 2 == 0])
#     odd_sum = sum([int(x) for x in num_list if int(x) % 2 != 0])
#     return f'Odd sum = {odd_sum}, Even sum = {even_sum}'
#
#
# print(even_odd_sum(number))

# # 05. Even Numbers
# line = [int(x) for x in input().split(' ')]
#
#
# def even_numbers(data):
#     return list(filter(lambda a: a % 2 == 0, data))
#
#
# print(even_numbers(line))

# # 06. Sort
# line = [int(x) for x in input().split(' ')]
#
#
# def even_numbers(data):
#     return list(sorted(data))
#
#
# print(even_numbers(line))

# # 07. Min Max and Sum
# line = [int(x) for x in input().split(' ')]
#
#
# def even_numbers(data):
#     return f'The minimum number is {min(line)}\n' \
#            f'The maximum number is {max(line)}\n' \
#            f'The sum number is: {sum(line)}'
#
#
# print(even_numbers(line))

# # 08. Palindrome Integers
# line = [x for x in input().split(', ')]
#
#
# def palindrome(data):
#     result = []
#     for el in data:
#         if el == el[::-1]:
#             result.append('True')
#         else:
#             result.append('False')
#     return '\n'.join(result)
#
#
# print(palindrome(line))

# # 09. Password Validator
# password = list(input())
#
#
# def pass_validator(line):
#     result = []
#     if not 6 <= len(line) <= 10:
#         result.append('Password must be between 6 and 10 characters')
#     for c in password:
#         if not c.isalnum():
#             result.append('Password must consist only of letters and digits')
#             break
#     digits = [x for x in password if x.isdigit()]
#     if len(digits) < 2:
#         result.append('Password must have at least 2 digits')
#     if result:
#         return '\n'.join(result)
#     return 'Password is valid'
#
#
# print(pass_validator(password))

# # 10. Perfect Number
# number = int(input())
#
#
# def perfect(num):
#     divisors = [x for x in range(1, num) if num % x == 0]
#     if sum(divisors) == number:
#         return 'We have a perfect number!'
#     return "It's not so perfect."
#
#
# print(perfect(number))

# # 11. Loading Bar
# number = int(input())
#
#
# def loading(num):
#     if num != 100:
#         return f"{num}% [{((num // 10) * '%') + (10 - (num // 10)) * '.'}]\nStill loading..."
#     return f"100% Complete!\n[{10 * '%'}]"
#
#
# print(loading(number))

# # 12. Factorial Division
# a, b = int(input()), int(input())
#
#
# def factorial(x, y):
#     ff, sf = 1, 1
#     for i in range(x, 0, -1):
#         ff *= i
#     for j in range(y, 0, -1):
#         sf *= j
#     return f'{(ff / sf):.2f}'
#
#
# print(factorial(a, b))


# # # More Exercises

# # 01. Data Types
# data, value = input(), input()
#
#
# def data_types(data_type, data_value):
#     if data_type == 'int':
#         return int(data_value) * 2
#     if data_type == 'real':
#         return f'{(float(data_value) * 1.5):.2f}'
#     return f'${data_value}$'
#
#
# print(data_types(data, value))

# # 02. Center Point
# from math import sqrt, floor
# x, y, z, w = float(input()), float(input()), float(input()), float(input())
#
#
# def center_point(a, b, c, d):
#     f_dist = sqrt(a ** 2 + b ** 2)
#     s_dist = sqrt(c ** 2 + d ** 2)
#     closer = min([f_dist, s_dist])
#     points = {f_dist: [a, b], s_dist: [c, d]}
#     return f'({floor(points[closer][0])}, {floor(points[closer][1])})'
#
#
# print(center_point(x, y, z, w))

# # 03. Longer Line
# from math import sqrt, floor
# s, t, u, v, w, x, y, z = float(input()), float(input()), float(input()), float(input()), \
#                          float(input()), float(input()), float(input()), float(input())
#
#
# def longer_line(a, b, c, d, e, f, g, h):
#     f_length = sqrt((a - c) ** 2 + (b - d) ** 2)
#     s_length = sqrt((e - g) ** 2 + (f - h) ** 2)
#     if f_length >= s_length:
#         k, l, m, n = a, b, c, d
#     else:
#         k, l, m, n = e, f, g, h
#     f_to_zero = sqrt(k ** 2 + l ** 2)
#     s_to_zero = sqrt(m ** 2 + n ** 2)
#     if f_to_zero <= s_to_zero:
#         result = f'({floor(k)}, {floor(l)})({floor(m)}, {floor(n)})'
#     else:
#         result = f'({floor(m)}, {floor(n)})({floor(k)}, {floor(l)})'
#     return result
#
#
# print(longer_line(s, t, u, v, w, x, y, z))

# # 04. Tribonacci Sequence
# number = int(input())
#
#
# def tribonacci(n):
#     line = [1, 1, 2]
#     if n < len(line):
#         line = line[:n]
#     elif n == len(line):
#         line = line
#     else:
#         for i in range(len(line), n):
#             line.append(sum(line[-3:]))
#     return ' '.join(str(x) for x in line)
#
#
# print(tribonacci(number))

# # 05. Multiplication Sign
# a, b, c = int(input()), int(input()), int(input())
#
#
# def multiplication_sign(x, y, z):
#     numbers = [x, y, z]
#     negatives = [j for j in numbers if j < 0]
#     if 0 in numbers:
#         return 'zero'
#     if len(negatives) % 2 != 0:
#         return 'negative'
#     return 'positive'
#
#
# print(multiplication_sign(a, b, c))