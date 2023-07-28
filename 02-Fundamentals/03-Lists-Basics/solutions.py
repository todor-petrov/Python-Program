# # # Lab

# # 01. Strange Zoo
# tail, body, head = input(), input(), input()
# print([head, body, tail])

# # 02. Courses
# number = int(input())
# courses = []
# for _ in range(number):
#     courses.append(input())
# print(courses)

# # 03. List Statistics
# number = int(input())
# positives, negatives = [], []
# for _ in range(number):
#     integer = int(input())
#     if integer >= 0:
#         positives.append(integer)
#     else:
#         negatives.append(integer)
# print(positives)
# print(negatives)
# print(f'Count of positives: {len(positives)}\nSum of negatives: {sum(negatives)}')

# # 04. Search
# number, word = int(input()), input()
# lines, selected = [], []
# for _ in range(number):
#     line = input()
#     lines.append(line)
#     if word in line:
#         selected.append(line)
# print(f'{lines}\n{selected}')

# # 05. Numbers Filter
# number = int(input())
# numbers = []
# for _ in range(number):
#     numbers.append(int(input()))
# command = input()
# commands = {
#     'even':     list(filter(lambda result: result % 2 == 0, numbers)),
#     'odd':      list(filter(lambda result: result % 2 != 0, numbers)),
#     'negative': list(filter(lambda result: result < 0, numbers)),
#     'positive': list(filter(lambda result: result >= 0, numbers))
# }
# print(commands[command])


# # # Exercise

# # 01. Invert Values
# print([-1 * int(x) for x in input().split(' ')])

# # 02. Multiples List
# factor, count = int(input()), int(input())
# print([factor * i for i in range(1, count + 1)])

# # 03. Football Cards
# red_cards = input().split(' ')
# a_team = [f'A-{i}' for i in range(1, 12)]
# b_team = [f'B-{i}' for i in range(1, 12)]
# game_was_terminated = False
# for card in red_cards:
#     if card.startswith('A') and card in a_team:
#         a_team.pop(a_team.index(card))
#     elif card.startswith('B') and card in b_team:
#         b_team.pop(b_team.index(card))
#     if len(a_team) < 7 or len(b_team) < 7:
#         game_was_terminated = True
#         break
# print(f'Team A - {len(a_team)}; Team B - {len(b_team)}')
# if game_was_terminated:
#     print('Game was terminated')

# # 04. Number Beggars
# coins, beggars = [int(x) for x in (input().split(', '))], [0 for x in range(int(input()))]
# for i in range(len(beggars)):
#     for j in range(i, len(coins), len(beggars)):
#         beggars[i] += coins[j]
# print(beggars)

# # 05. Faro Shuffle
# line, shuffles = input().split(' '), int(input())
# deck = line
# for shuffle in range(shuffles):
#     first, second, current_deck = deck[:int(len(line) / 2)], deck[int(len(line) / 2):], []
#     for i in range(len(first)):
#         current_deck.append(first[i]), current_deck.append(second[i])
#     deck = current_deck
# print(deck)

# # 06. Survival of the Biggest
# line, count = [int(x) for x in input().split(' ')], int(input())
# # # solution # 1
# # while count != 0:
# #     line.pop(line.index(min(line)))
# #     count -= 1
# # # solution # 2
# for i in range(count):
#     line.pop(line.index(min(line)))
# print(', '.join(str(x) for x in line))

# # 07. Easter Gifts
# gifts, token = input().split(' '), input()
# while token != 'No Money':
#     data = token.split(' ')
#     command, gift = data[0], data[1]
#     if command == 'OutOfStock' and gift in gifts:
#         gifts[:] = [x if x != gift else None for x in gifts]
#     elif command == 'Required' and 0 <= int(data[2]) < len(gifts):
#         gifts[int(data[2])] = gift
#     elif command == 'JustInCase':
#         gifts[-1] = gift
#     token = input()
# print(' '.join(x for x in gifts if x is not None))

# # 08. Seize the Fire
# fires, water = input().split('#'), int(input())
# effort, total_fire, cells = 0, 0, ['Cells:']
# ranges = {'High': [81, 125], 'Medium': [51, 80], 'Low': [1, 50]}
# for fire in fires:
#     cell, needed_water = fire.split(' = ')
#     needed_water = int(needed_water)
#     if cell in ranges and ranges[cell][0] <= needed_water <= ranges[cell][1] and needed_water <= water:
#         cells.append(f' - {needed_water}')
#         total_fire += needed_water
#         effort += (needed_water * 0.25)
#         water -= needed_water
# print('\n'.join(cells))
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {total_fire}')

# # 09. Hello, France
# line = input().split('|')
# budget = int(input())
# ticket, profits = 150, []
# sold_items = []
# items = {'Clothes': 50.00, 'Shoes': 35.00, 'Accessories': 20.50}
# for element in line:
#     info = element.split('->')
#     item, price = info[0], float(info[1])
#     if price <= items[item] and price <= budget:
#         budget -= price
#         profits.append(price * 0.4)
#         sold_items.append(price * 1.4)
# total_money = budget + sum(sold_items)
# items_result = []
# for i in sold_items:
#     items_result.append(f'{i:.2f}')
# print(' '.join(items_result))
# print(f'Profit: {sum(profits):.2f}')
# if total_money >= ticket:
#     print('Hello, France!')
# else:
#     print('Not enough money.')

# # 10. Bread Factory
# events = input().split('|')
# energy, coins = 100, 100
# max_energy, closed = 100, False
# for command in events:
#     data = command.split('-')
#     event, number = data[0], int(data[1])
#     if event == 'rest':
#         if energy + number > max_energy:
#             number = max_energy - energy
#         energy += number
#         print(f'You gained {number} energy.')
#         print(f'Current energy: {energy}.')
#     elif event == 'order':
#         if energy - 30 >= 0:
#             energy -= 30
#             coins += number
#             print(f'You earned {number} coins.')
#         else:
#             energy += 50
#             print('You had to rest!')
#     else:
#         if coins >= number:
#             coins -= number
#             print(f'You bought {event}.')
#         else:
#             closed = True
#             print(f'Closed! Cannot afford {event}.')
#             break
# if not closed:
#     print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')


# # # More Exercises

# # 01. Zeros to Back
# numbers = list(map(int, input().split(', ')))
# result = [x for x in numbers if x != 0]
# zeroes = [x for x in numbers if x == 0]
# result = result + zeroes
# print(result)

# # 02. Messaging
# numbers = input().split()
# string = input()
# indices, message = [], ''
# for el in numbers:
#     current_i = sum([int(el[i]) for i in range(len(el))])
#     indices.append(current_i)
# while len(indices) > 0:
#     for index in indices:
#         if index > len(string):
#             while index > len(string):
#                 index -= len(string)
#         message += string[index]
#         string = string[:index] + string[index + 1:]
#         del indices[0]
#         break
# print(message)

# # 03. Car Race
# sequence = list(map(int, input().split()))
# mid_i = len(sequence) // 2
# left_trace = sequence[:mid_i]
# right_trace = sequence[mid_i + 1:][::-1]
# left_time, right_time = 0, 0
# for i in range(len(left_trace)):
#     if left_trace[i] != 0:
#         left_time += left_trace[i]
#     else:
#         left_time *= 0.8
#     if right_trace[i] != 0:
#         right_time += right_trace[i]
#     else:
#         right_time *= 0.8
# if left_time < right_time:
#     print(f'The winner is left with total time: {left_time:.1f}')
# else:
#     print(f'The winner is right with total time: {right_time:.1f}')

# # 04. Josephus Permutation
# circle = input().split(' ')
# kill_count = int(input())
# result = []
# counter = 0
#
# index = 0
# while len(circle) > 0:
#     counter += 1
#
#     if counter % kill_count == 0:
#         result.append(circle.pop(index))
#     else:
#         index += 1
#
#     if index >= len(circle):
#         index = 0
#
# print(str(result).replace(' ', '').replace('\'', ''))

# # 05. Tic-Tac-Toe
# r_1 = input().split()
# r_2 = input().split()
# r_3 = input().split()
# row_1 = ''
# row_2 = ''
# row_3 = ''
# final = []
# condition = False
# result = ''
# for i in range(3):
#     row_1 += r_1[i]
#     row_2 += r_2[i]
#     row_3 += r_3[i]
# final.append(row_1)
# final.append(row_2)
# final.append(row_3)
# column_1 = r_1[0] + r_2[0] + r_3[0]
# column_2 = r_1[1] + r_2[1] + r_3[1]
# column_3 = r_1[2] + r_2[2] + r_3[2]
# final.append(column_1)
# final.append(column_2)
# final.append(column_3)
# diagonal_1 = row_1[0] + row_2[1] + row_3[2]
# diagonal_2 = row_1[2] + row_2[1] + row_3[0]
# final.append(diagonal_1)
# final.append(diagonal_2)
# for el in final:
#     if el == '111':
#         condition = True
#         result = 'First player won'
#         break
#     elif el == '222':
#         condition = True
#         result = 'Second player won'
#         break
# if condition:
#     print(f'{result}')
# else:
#     print('Draw!')

# # 06. List Manipulator
# integers = [int(x) for x in input().split(' ')]
# token = input()
# while token != 'end':
#     data = token.split(' ')
#     action = data[0]
#     if action == 'exchange':
#         index = int(data[1])
#         if 0 <= index < len(integers):
#             if 0 <= index < len(integers) - 1:
#                 first, second = integers[:(index + 1)], integers[(index + 1):]
#                 integers = second + first
#         else:
#             print('Invalid index')
#     elif action == 'max':
#         if data[1] == 'even':
#             evens = [x for x in integers if x % 2 == 0]
#             if evens:
#                 max_even_el, max_even_el_index = evens[0], 0
#                 for i in range(len(integers)):
#                     if integers[i] >= max_even_el and integers[i] % 2 == 0:
#                         max_even_el = integers[i]
#                         max_even_el_index = i
#                 print(max_even_el_index)
#             else:
#                 print('No matches')
#         elif data[1] == 'odd':
#             odds = [x for x in integers if x % 2 != 0]
#             if odds:
#                 max_odd_el, max_odd_el_index = odds[0], 0
#                 for i in range(len(integers)):
#                     if integers[i] >= max_odd_el and integers[i] % 2 != 0:
#                         max_odd_el = integers[i]
#                         max_odd_el_index = i
#                 print(max_odd_el_index)
#             else:
#                 print('No matches')
#     elif action == 'min':
#         if data[1] == 'even':
#             evens = [x for x in integers if x % 2 == 0]
#             if evens:
#                 min_even_el, min_even_el_index = evens[0], 0
#                 for i in range(len(integers)):
#                     if integers[i] <= min_even_el and integers[i] % 2 == 0:
#                         min_even_el = integers[i]
#                         min_even_el_index = i
#                 print(min_even_el_index)
#             else:
#                 print('No matches')
#         elif data[1] == 'odd':
#             odds = [x for x in integers if x % 2 != 0]
#             if odds:
#                 min_odd_el, min_odd_el_index = odds[0], 0
#                 for i in range(len(integers)):
#                     if integers[i] <= min_odd_el and integers[i] % 2 != 0:
#                         min_odd_el = integers[i]
#                         min_odd_el_index = i
#                 print(min_odd_el_index)
#             else:
#                 print('No matches')
#     elif action == 'first':
#         count = int(data[1])
#         if data[2] == 'even':
#             if len(integers) < count:
#                 print('Invalid count')
#             else:
#                 evens = [x for x in integers if x % 2 == 0]
#                 if len(evens) <= count:
#                     print(evens)
#                 else:
#                     print(evens[:count])
#         elif data[2] == 'odd':
#             if len(integers) < count:
#                 print('Invalid count')
#             else:
#                 odds = [x for x in integers if x % 2 != 0]
#                 if len(odds) <= count:
#                     print(odds)
#                 else:
#                     print(odds[:count])
#     elif action == 'last':
#         count = int(data[1])
#         if data[2] == 'even':
#             if len(integers) < count:
#                 print('Invalid count')
#             else:
#                 evens = [x for x in integers if x % 2 == 0]
#                 if len(evens) <= count:
#                     print(evens)
#                 else:
#                     print(evens[-count:])
#         elif data[2] == 'odd':
#             if len(integers) < count:
#                 print('Invalid count')
#             else:
#                 odds = [x for x in integers if x % 2 != 0]
#                 if len(odds) <= count:
#                     print(odds)
#                 else:
#                     print(odds[-count:])
#     token = input()
# print(integers)