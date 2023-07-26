# # # Lab

# # 01. Count Same Values
# line = [float(x) for x in input().split(' ')]
# unique, result = [], tuple()
# for el in line:
#     if el not in unique:
#         unique.append(el)
#         result += ((f'{el} - {line.count(el)} times',),)
# for t in result:
#     print(*t)

# # 02. Students' Grades
# number, students, result = int(input()), {}, []
# for student in range(number):
#     name, grade = input().split(' ')
#     if name not in students:
#         students[name] = []
#     students[name].append(float(grade))
# for student, grades in students.items():
#     print(f"{student} -> {' '.join(str(f'{x:.2f}') for x in grades)} "
#           f"(avg: {(sum(grades) / len(grades)):.2f})")

# # 03. Record Unique Names
# print('\n'.join(set([input() for x in range(int(input()))])))

# # 04. Parking Lot
# number, lot = int(input()), set()
# for i in range(number):
#     action, car = input().split(', ')
#     if action == 'IN' and car not in lot:
#         lot.add(car)
#     elif action == 'OUT' and car in lot:
#         lot.remove(car)
# print('\n'.join(c for c in lot)) if lot else print('Parking Lot is Empty')

# # 05. SoftUni Party
# guests = set([input() for x in range(int(input()))])
# guest = input()
# while guest != 'END' and guest in guests:
#     guests.remove(guest)
#     guest = input()
# guests = sorted(tuple(guests))
# print(len(guests))
# print('\n'.join(x for x in guests))


# # # Exercise

# # 01. Unique Usernames
# print('\n'.join(set(input() for x in range(int(input())))))

# # 02. Sets of Elements
# n, m = [int(x) for x in (input()).split(' ')]
# first = [int(input()) for x in range(n)]
# second = [int(input()) for x in range(m)]
# print('\n'.join(str(x) for x in set(first).intersection(second)))

# # 03. Periodic Table
# number, data = int(input()), []
# for i in range(number):
#     data.extend(input().split(' '))
# result = set(data)
# [print(item) for item in result]

# # 04. Count Symbols
# line = [x for x in input()]
# unique = sorted(set(line))
# for el in unique:
#     print(f'{el}: {line.count(el)} time/s')

# # 05. Longest Intersection
# number, result, max_intersection = int(input()), [], set()
# for i in range(number):
#     data = input().split('-')
#     [fs, fe] = [int(x) for x in data[0].split(',')]
#     ss, se = [int(x) for x in data[1].split(',')]
#     first = set([int(x) for x in range(fs, fe + 1)])
#     second = set([int(x) for x in range(ss, se + 1)])
#     current_intersection = first.intersection(second)
#     if len(current_intersection) > len(max_intersection):
#         max_intersection = current_intersection
# result = f"[{', '.join(str(x) for x in max_intersection)}]"
# length = len(max_intersection)
# print(f"Longest intersection is {result} with length {length}")

# # 06. Battle of Names
# number, even, odd = int(input()), set(), set()
# for i in range(1, number + 1):
#     value = int(sum([ord(i) for i in input()]) / i)
#     even.add(value) if value % 2 == 0 else odd.add(value)
# if sum(even) == sum(odd):
#     print(', '.join([str(int(x)) for x in (odd.union(even))]))
# elif sum(odd) > sum(even):
#     print(', '.join([str(int(x)) for x in odd.difference(even)]))
# else:
#     print(', '.join([str(int(x)) for x in (odd.symmetric_difference(even))]))


# # # Stacks, Queues, Tuples and Sets - Exercise

# # 01. Numbers

# first = set([int(x) for x in input().split(' ')])
# second = set([int(x) for x in input().split(' ')])
# number = int(input())
# for i in range(number):
#     data = input().split(' ')
#     action = data[0]
#     if action == 'Add' and data[1] == 'First':
#         first.update([int(x) for x in data[2:]])
#     elif action == 'Add' and data[1] == 'Second':
#         second.update([int(x) for x in data[2:]])
#     elif action == 'Remove' and data[1] == 'First':
#         numbers = [int(x) for x in data[2:]]
#         [first.remove(x) for x in numbers if x in first]
#     elif action == 'Remove' and data[1] == 'Second':
#         numbers = [int(x) for x in data[2:]]
#         [second.remove(x) for x in numbers if x in second]
#     elif action == 'Check':
#         if first.issubset(second) or second.issubset(first):
#             print('True')
#         else:
#             print('False')
# print(', '.join([str(x) for x in sorted(first)]))
# print(', '.join([str(x) for x in sorted(second)]))

# 02. Expression Evaluator
# from collections import deque
# from math import floor
#
# line = deque(input().split(' '))
# operators = ['+', '-', '*', '/']
# numbers, flag = [], False
# while len(line) > 0:
#     element = line.popleft()
#     if len(line) == 0:
#         flag = True
#     if element not in operators:
#         numbers.append(int(element))
#     else:
#         if element == '+':
#             line.appendleft(str(sum(numbers)))
#             numbers = []
#         elif element == '-':
#             for i in range(1, len(numbers)):
#                 numbers[0] -= numbers[i]
#             line.appendleft(str(numbers[0]))
#             numbers = []
#         elif element == '*':
#             for i in range(1, len(numbers)):
#                 numbers[0] *= numbers[i]
#             line.appendleft(str(numbers[0]))
#             numbers = []
#         elif element == '/':
#             for i in range(1, len(numbers)):
#                 numbers[0] /= numbers[i]
#             line.appendleft(str(floor(numbers[0])))
#             numbers = []
#     if flag:
#         break
# print(line[0])

# # 03. Milkshakes
# from collections import deque
#
# chocolates = list(map(int, input().split(', ')))
# milk_cups = deque(map(int, input().split(', ')))
# milkshakes = 0
#
# while milkshakes < 5 and chocolates and milk_cups:
#     flag = False
#     if chocolates[-1] <= 0:
#         chocolates.pop()
#         flag = True
#
#     if milk_cups[0] <= 0:
#         milk_cups.popleft()
#         flag = True
#
#     if flag:
#         continue
#
#     if chocolates[-1] == milk_cups[0]:
#         milkshakes += 1
#         chocolates.pop()
#         milk_cups.popleft()
#     else:
#         milk_cups.append(milk_cups.popleft())
#         chocolates[-1] -= 5
#
# if milkshakes == 5:
#     print('Great! You made all the chocolate milkshakes needed!')
# else:
#     print('Not enough milkshakes.')
# print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
# print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")

# # 04. Honey
# from collections import deque
#
# bees = deque(map(int, input().split()))
# nectar = list(map(int, input().split()))
# symbols = deque(input().split())
# total_honey = 0
# while bees and nectar:
#     if nectar[-1] >= bees[0]:
#         symbol = symbols.popleft()
#         collected_nectar, bee = nectar.pop(), bees.popleft()
#         if symbol == '+':
#             total_honey += abs(bee + collected_nectar)
#         elif symbol == '-':
#             total_honey += abs(bee - collected_nectar)
#         elif symbol == '*':
#             total_honey += abs(bee * collected_nectar)
#         else:
#             if collected_nectar == 0 or bee == 0:
#                 continue
#             total_honey += abs(bee / collected_nectar)
#
#     else:
#         nectar.pop()
#
# print(f'Total honey made: {total_honey}')
#
# if bees:
#     print(f"Bees left: {', '.join(map(str, bees))}")
# if nectar:
#     print(f"Nectar left: {', '.join(map(str, nectar))}")

# # 05. Santa's Present Factory
# from collections import deque
#
# boxes = [int(x) for x in input().split()]
# magic_levels = deque([int(x) for x in input().split()])
#
# presents = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle'
# }
#
# crafted_presents = {}
# while boxes and magic_levels:
#     box = boxes.pop()
#     magic_level = magic_levels.popleft()
#
#     result = box * magic_level
#
#     if result in presents:
#         toy = presents[result]
#         if toy in crafted_presents:
#             crafted_presents[toy] += 1
#         else:
#             crafted_presents[toy] = 1
#     elif result < 0:
#         boxes.append(box + magic_level)
#     elif result > 0:
#         boxes.append(box + 15)
#     else:
#         if box == 0 and magic_level == 0:
#             continue
#         if box == 0:
#             magic_levels.appendleft(magic_level)
#         else:
#             boxes.append(box)
# if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
#         ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
#     print(f'The presents are crafted! Merry Christmas!')
# else:
#     print(f'No presents this Christmas!')
# if boxes:
#     print(f"Materials left: {', '.join([str(x) for x in reversed(boxes)])}")
# if magic_levels:
#     print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
# for present, count in sorted(crafted_presents.items()):
#     print(f'{present}: {count}')

# # 06. Paint Colors
# from collections import deque
#
# line = deque(input().split())
# colours = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
# secondary_colours = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
# final = []
# while line:
#     if len(line) > 1:
#         a = line.popleft()
#         b = line.pop()
#         if a + b in colours:
#             final.append(a + b)
#         elif b + a in colours:
#             final.append(b + a)
#         else:
#             a = a[:-1]
#             b = b[:-1]
#             if a:
#                 line.insert(len(line) // 2, a)
#             if b:
#                 line.insert(len(line) // 2, b)
#     else:
#         a = line.pop()
#         if a in colours:
#             final.append(a)
#         else:
#             a = a[:-1]
#             if a:
#                 line.append(a)
# for colour, main_colours in secondary_colours.items():
#     if colour in final and (main_colours[0] not in final or main_colours[1] not in final):
#         final.remove(colour)
# print(final)