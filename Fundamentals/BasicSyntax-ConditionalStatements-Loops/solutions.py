# # # Lab

# # 01. Number Definer
# number, result = float(input()), ''
# if 0 < abs(number) < 1:
#     result = 'small '
# elif 1000000 < abs(number):
#     result = 'large '
# if number == 0:
#     result = 'zero'
# elif number > 0:
#     result += 'positive'
# else:
#     result += 'negative'
# print(result)

# # 02. Largest of Three Numbers
# print(max([int(input()), int(input()), int(input())]))

# # 03. Word Reverse
# print(input()[::-1])

# # 04. Even Numbers
# number = int(input())
# odd_is_found = False
# for _ in range(number):
#     integer = int(input())
#     if integer % 2 != 0:
#         print(f'{integer} is odd!')
#         odd_is_found = True
#         break
# if not odd_is_found:
#     print('All numbers are even.')

# # 05. Number Between 1 and 100
# while True:
#     number = float(input())
#     if 1 <= number <= 100:
#         print(f'The number {number} is between 1 and 100')
#         break

# # 06. Shopping
# budget, command = int(input()), input()
# went_in_overdraft = False
# while command != 'End':
#     price = int(command)
#     if budget < price:
#         went_in_overdraft = True
#         print('You went in overdraft!')
#         break
#     budget -= price
#     command = input()
# if not went_in_overdraft:
#     print('You bought everything needed.')

# # 07. Patterns
# number = int(input())
# for i in range(1, number + 1):
#     print('*' * i)
# for j in range(number - 1, 0, -1):
#     print('*' * j)


# # # Exercise

# # 01. Jenny's Secret Message
# name, my_love = input(), 'Johnny'
# print(f'Hello, {name}!' if name != my_love else 'Hello, my love!')

# # 02. Drink something
# age = int(input())
# drinks = {'toddy': [1, 14], 'coke': [15, 18], 'beer': [19, 21], 'whisky': [22, 100]}
# for drink, years in drinks.items():
#     if years[0] <= age <= years[1]:
#         print(f'drink {drink}')
#         break

# # 03. Chat Codes
# cycles = int(input())
# for cycle in range(cycles):
#     number = int(input())
#     if number == 88:
#         print('Hello')
#     elif number == 86:
#         print('How are you?')
#     elif number < 88 and number != 86:
#         print('GREAT!')
#     elif 88 < number:
#         print('Bye.')

# # 04. Maximum Miltiple
# divisor, bound = int(input()), int(input())
# max_integer = 0
# for i in range(bound + 1):
#     if i % divisor == 0 and bound >= i > 0:
#         if max_integer < i:
#             max_integer = i
# print(max_integer)

# # 05. Orders
# number_of_orders = int(input())
# ranges = {'price_per_day': [0.01, 100.00], 'days': [1, 31], 'capsules': [1, 2000]}
# total_price = 0.0
# for order in range(number_of_orders):
#     price_per_capsule, days, capsules = float(input()), int(input()), int(input())
#     if ranges['price_per_day'][0] <= price_per_capsule <= ranges['price_per_day'][1] and \
#        ranges['days'][0] <= days <= ranges['days'][1] and \
#        ranges['capsules'][0] <= capsules <= ranges['capsules'][1]:
#         current_price = price_per_capsule * days * capsules
#         total_price += current_price
#         print(f'The price for the coffee is: ${current_price:.2f}')
# print(f'Total: ${total_price:.2f}')

# # 06. String Pureness
# number = int(input())
# for i in range(number):
#     line = input()
#     if ',' in line or '.' in line or '_' in line:
#         print(f'{line} is not pure!')
#     else:
#         print(f'{line} is pure.')

# # 07. Double Char
# line = input()
# while line != 'End':
#     if line != 'SoftUni':
#         print(''.join([x * 2 for x in line]))
#     line = input()

# # 08. How Much Coffee Do You Need?
# command, max_coffees, coffees_count = input(), 5, 0
# events = ['coding', 'CODING', 'dog', 'DOG', 'cat', 'CAT', 'movie', 'MOVIE']
# while command != 'END':
#     if command in events:
#         if command.islower():
#             coffees_count += 1
#         elif command.isupper():
#             coffees_count += 2
#     command = input()
# if coffees_count <= max_coffees:
#     print(coffees_count)
# else:
#     print('You need extra sleep')

# # 09. Sorting Hat
# name = input()
# voldemort = False
# while name != 'Welcome!':
#     if name == 'Voldemort':
#         voldemort = True
#         print('You must not speak of that name!')
#         break
#     else:
#         if len(name) < 5:
#             print(f'{name} goes to Gryffindor.')
#         elif len(name) == 5:
#             print(f'{name} goes to Slytherin.')
#         elif len(name) == 6:
#             print(f'{name} goes to Ravenclaw.')
#         else:
#             print(f'{name} goes to Hufflepuff.')
#     name = input()
# if not voldemort:
#     print('Welcome to Hogwarts.')

# # 10. Mutate Strings
# first, second = list(input()), list(input())
# for i in range(len(first)):
#     if first[i] != second[i]:
#         first[i] = second[i]
#         print(''.join(first))

# # 11. Easter Bread
# budget, flour = float(input()), float(input())
# eggs, milk = flour * 0.75, flour * 1.25
# loaves = int(budget / (flour + eggs + milk * 0.25))
# money_left = budget - (loaves * (flour + eggs + milk * 0.25))
# colored_eggs = 0
# for i in range(1, loaves + 1):
#     colored_eggs += 3
#     if i % 3 == 0:
#         colored_eggs -= (i - 2)
# print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs '
#       f'and {money_left:.2f}BGN left.')

# # 12. Christmas Spirit
# quantity, days = int(input()), int(input())
# budget, spirit = 0, 0
# decorations = {'Ornament Set': [2, 5],
#                'Tree Skirt': [5, 3],
#                'Tree Garland': [3, 10],
#                'Tree Lights': [15, 17]}
# for day in range(1, days + 1):
#     if day % 11 == 0:
#         quantity += 2
#     if day % 2 == 0:
#         budget += (decorations['Ornament Set'][0] * quantity)
#         spirit += decorations['Ornament Set'][1]
#     if day % 3 == 0:
#         budget += (decorations['Tree Skirt'][0] * quantity)
#         budget += (decorations['Tree Garland'][0] * quantity)
#         spirit += decorations['Tree Skirt'][1]
#         spirit += decorations['Tree Garland'][1]
#     if day % 5 == 0:
#         budget += (decorations['Tree Lights'][0] * quantity)
#         spirit += decorations['Tree Lights'][1]
#         if day % 3 == 0:
#             spirit += 30
#     if day % 10 == 0:
#         spirit -= 20
#         budget += decorations['Tree Skirt'][0]
#         budget += decorations['Tree Garland'][0]
#         budget += decorations['Tree Lights'][0]
# if days % 10 == 0:
#     spirit -= 30
# print(f'Total cost: {budget}')
# print(f'Total spirit: {spirit}')