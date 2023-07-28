# # # Lab


# # 01. Concat Names
# first_name, last_name, delimiter = input(), input(), input()
# print(f'{first_name}{delimiter}{last_name}')

# # 02. Convert Meters to Kilometers
# meters = int(input())
# kilometers = meters / 1000
# print(f'{kilometers:.2f}')

# # 03. Pounds to Dollars
# pounds = int(input())
# dollars = pounds * 1.31
# print(f'{dollars:.3f}')

# # 04. Centuries to Minutes
# centuries = int(input())
# years = centuries * 100
# days = int(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
# print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

# # 05. Special Numbers
# integer = int(input())
# special = [5, 7, 11]
# for i in range(1, integer + 1):
#     current_sum = sum([int(j) for j in str(i)])
#     if current_sum in special:
#         print(f'{i} -> True')
#     else:
#         print(f'{i} -> False')

# 06. Next Happy Year
# year = int(input())
# while True:
#     year += 1
#     current_year_as_list = list(str(year))
#     current_year_as_set = set(str(year))
#     if len(current_year_as_list) == len(current_year_as_set):
#         print(year)
#         break


# # # Exercise

# # 01. Integer Operations
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print((a + b) // c * d)

# # 02. Chars to String
# print(input() + input() + input())

# # 03. Elevator
# people, capacity = int(input()), int(input())
# courses = 0
# while people:
#     courses += 1
#     people -= capacity
#     if people <= 0:
#         break
# print(courses)

# # 04. Sum of Chars
# lines, total_sum = int(input()), 0
# for i in range(lines):
#     alpha = input()
#     total_sum += ord(alpha)
# print(f'The sum equals: {total_sum}')

# # 05. Print Part of the ASCII Table
# start, end = int(input()), int(input())
# result = []
# for i in range(start, end + 1):
#     result.append(chr(i))
# print(' '.join(result))

# # 06. Triples of Latin Letters
# integer = int(input())
# for i in range(97, 97 + integer):
#     for j in range(97, 97 + integer):
#         for k in range(97, 97 + integer):
#             print(f'{chr(i)}{chr(j)}{chr(k)}')

# # 07. Water Overflow
# capacity, tank = 255, 0
# lines = int(input())
# for i in range(lines):
#     liters = int(input())
#     if liters <= capacity - tank:
#         tank += liters
#     else:
#         print('Insufficient capacity!')
# print(tank)

# # 08. Party Profit
# from math import floor
# group, days, coins = int(input()), int(input()), 0
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         group -= 2
#     if day % 15 == 0:
#         group += 5
#     coins += (50 - group * 2)
#     if day % 3 == 0:
#         coins -= (group * 3)
#     if day % 5 == 0:
#         coins += (group * 20)
#         if day % 3 == 0:
#             coins -= (group * 2)
# coins_per_person = floor(coins / group)
# print(f'{group} companions received {coins_per_person} coins each.')

# # 09. Snowballs
# snowballs = int(input())
# snowball_weight, snowball_time, snowball_value, snowball_quality = 0, 0, 0, 0
#
# for snowball in range(snowballs):
#     weight, time, quality = int(input()), int(input()), int(input())
#     value = (weight / time) ** quality
#     if snowball_value < value:
#         snowball_weight, snowball_time, snowball_value, snowball_quality = \
#             weight, time, value, quality
# print(f'{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})')

# # 10. Gladiator Expenses
# lost, helmet, sword, shield, armor = \
#     int(input()), float(input()), float(input()), float(input()), float(input())
# expenses, broken_shields_count = 0, 0
# for fight in range(1, lost + 1):
#     if fight % 2 == 0:
#         expenses += helmet
#     if fight % 3 == 0:
#         expenses += sword
#         if fight % 2 == 0:
#             expenses += shield
#             broken_shields_count += 1
#             if broken_shields_count == 2:
#                 expenses += armor
#                 broken_shields_count = 0
# print(f'Gladiator expenses: {expenses:.2f} aureus ')


# # # More Exercises

# # 01. Exchange Integers
# a, b = int(input()), int(input())
# print(f'Before:\na = {a}\nb = {b}')
# print(f'After:\na = {b}\nb = {a}')

# # 02. Prime Number Checker
# number = int(input())
# the_number_is_prime = True
# for i in range(2, number):
#     if number % i == 0:
#         the_number_is_prime = False
#         print('False')
#         break
# if the_number_is_prime:
#     print('True')

# # 03. Decrypting Messages
# key, lines = int(input()), int(input())
# result = ''
# for _ in range(lines):
#     character = ord(input())
#     result += chr(character + key)
# print(result)

# # 04. Balanced Brackets
# lines = int(input())
# pair, count = '', 0
# for _ in range(lines):
#     char = input()
#     if char == '(' or char == ')':
#         pair += char
#         if pair == '()':
#             pair = ''
#             count += 1
# if pair == '' and count > 0:
#     print('BALANCED')
# else:
#     print('UNBALANCED')
