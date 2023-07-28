# # # Lab

# # 01. No Vowels
# line = list(input())
# vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
# result = [x for x in line if x not in vowels]
# print(''.join(result))

# # 02. Trains
# wagons = [0 for x in range(int(input()))]
# line = input()
# while line != 'End':
#     data = line.split(' ')
#     command = data[0]
#     if command == 'add':
#         wagons[-1] += int(data[1])
#     elif command == 'insert':
#         wagons[int(data[1])] += int(data[2])
#     else:
#         wagons[int(data[1])] -= int(data[2])
#     line = input()
# print(wagons)

# # 03. To-do List
# note = input()
# notes = {}
# while note != 'End':
#     data = note.split('-')
#     importance, task = int(data[0]), data[1]
#     notes[importance] = task
#     note = input()
# sorted_notes = {k: v for k, v in sorted(notes.items(), key=lambda item: item[0])}
# result = list(sorted_notes.values())
# print(result)

# # 04. Palindrome Strings
# line, palindrome = input().split(' '), input()
# palindromes = [x for x in line if x == x[::-1]]
# count = palindromes.count(palindrome)
# print(f'{palindromes}\nFound palindrome {count} times')

# # 05. Sorting Names
# names = input().split(', ')
# result = sorted(names, key=lambda x: (-len(x), x))
# print(result)

# # 06. Even Numbers
# numbers = [int(x) for x in input().split(', ')]
# result = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         result.append(i)
# print(result)

# # 07. The Office
# employee_happiness = [int(x) for x in input().split(' ')]
# factor = int(input())
# result = [x * factor for x in employee_happiness]
# average = sum(result) / len(result)
# happy_count = len([x for x in result if x >= average])
# if happy_count >= len(employee_happiness) / 2:
#     print(f'Score: {happy_count}/{len(employee_happiness)}. Employees are happy!')
# else:
#     print(f'Score: {happy_count}/{len(employee_happiness)}. Employees are not happy!')


# # # Exercise

# # 01. Which Are In?
# substrings = input().split(', ')
# strings = input().split(', ')
# result = []
# for substring in substrings:
#     for line in strings:
#         if substring in line and substring not in result:
#             result.append(substring)
# print(result)

# # 02. Next Version
# version = input().split('.')
# next_version_as_int = int(''.join(x for x in version)) + 1
# next_version = list(str(next_version_as_int))
# print('.'.join(next_version))

# # 03. Word Filter
# print('\n'.join([x for x in input().split(' ') if len(x) % 2 == 0]))

# # 04. Number Classification
# numbers = [int(x) for x in input().split(', ')]
# print('\n'.join([f"Positive: {', '.join(str(x) for x in numbers if x >= 0)}",
#                  f"Negative: {', '.join(str(x) for x in numbers if x < 0)}",
#                  f"Even: {', '.join(str(x) for x in numbers if x % 2 == 0)}",
#                  f"Odd: {', '.join(str(x) for x in numbers if x % 2 != 0)}"]))

# # 05. Office Chairs
# rooms = int(input())
# chairs_needed = False
# free_chairs = 0
# for i in range(1, rooms + 1):
#     room = input().split(' ')
#     chairs, people = len(room[0]), int(room[1])
#     if chairs < people:
#         needed_chairs = people - chairs
#         chairs_needed = True
#         print(f'{needed_chairs} more chairs needed in room {i}')
#     else:
#         free_chairs += (chairs - people)
# if not chairs_needed:
#     print(f'Game On, {free_chairs} free chairs left')

# # 06. Electron Distribution
# electrons = int(input())
# result, i = [], 0
# while electrons:
#     i += 1
#     current = 2 * (i ** 2)
#     if electrons - current >= 0:
#         electrons -= current
#         result.append(current)
#     else:
#         result.append(electrons)
#         electrons = 0
# print(result)

# # 07. Group of 10's
# numbers = [int(x) for x in input().split(', ')]
# groups, result = 0, {}
# if max(numbers) % 10 == 0:
#     groups = max(numbers) // 10
# else:
#     groups = max(numbers) // 10 + 1
# for i in range(1, groups + 1):
#     result[i * 10] = []
# for n in numbers:
#     for g in result:
#         if n <= g:
#             result[g].append(n)
#             break
# for gr in result:
#     print(f"Group of {gr}'s: {result[gr]}")

# # 08. Decipher This!
# from collections import deque
# line = input().split(' ')
# result = []
# for word in line:
#     current = deque(word)
#     ascii_n = ''
#     while True:
#         if current[0].isalpha():
#             break
#         else:
#             ascii_n += current.popleft()
#     first_letter = chr(int(ascii_n))
#     current[-1], current[0] = current[0], current[-1]
#     result.append(first_letter + ''.join(current))
# print(' '.join(result))

# # 09. Anonymous Threat
# line = input().split(' ')
# token = input()
# while token != '3:1':
#     data = token.split(' ')
#     command, i, j = data[0], int(data[1]), int(data[2])
#     if command == 'merge':
#         if i < 0:
#             i = 0
#         if j > len(line) - 1:
#             j = len(line) - 1
#         first, last = line[:i], line[(j + 1):]
#         merged = [''.join(line[i:(j + 1)])]
#         line = first + merged + last
#     else:
#         el_for_divide, first, last, divided = line[i], line[:i], [], []
#         if i != len(line) - 1:
#             last = line[(i + 1):]
#         p = len(el_for_divide) // j
#         for a in range(j):
#             if a == j - 1:
#                 divided.append(el_for_divide)
#                 break
#             divided.append(el_for_divide[:p])
#             el_for_divide = el_for_divide[p:]
#         line = first + divided + last
#     token = input()
# print(' '.join(line))

# # 10. Pokemon Don't Go
# pokemons = [int(x) for x in input().split(' ')]
# i = int(input())
# caught = []
# while pokemons:
#     if 0 <= i <= len(pokemons) - 1:
#         caught.append(pokemons.pop(i))
#         if not pokemons:
#             break
#     elif i < 0:
#         caught.append(pokemons[0])
#         pokemons[0] = pokemons[-1]
#     elif i > len(pokemons) - 1:
#         caught.append(pokemons[-1])
#         pokemons[-1] = pokemons[0]
#     n = caught[-1]
#     for j in range(len(pokemons)):
#         if pokemons[j] <= n:
#             pokemons[j] += n
#         else:
#             pokemons[j] -= n
#     i = int(input())
# print(sum(caught))

# # 11. SoftUni Course Planning
# courses = input().split(', ')
# token = input()
# exercises = []
# while token != 'course start':
#     data = token.split(':')
#     command, title = data[0], data[1]
#     if command == 'Add' and title not in courses:
#         courses.append(title)
#     elif command == 'Insert':
#         index = int(data[2])
#         if title not in courses:
#             start, end = courses[:index], courses[index:]
#             courses = start + [title] + end
#     elif command == 'Remove' and title in courses:
#         courses.remove(title)
#         if title in exercises:
#             exercises.remove(title)
#     elif command == 'Swap':
#         other_title = data[2]
#         if title in courses and other_title in courses:
#             i, j = courses.index(title), courses.index(other_title)
#             courses[i], courses[j] = courses[j], courses[i]
#     elif command == 'Exercise':
#         if title not in courses:
#             courses.append(title)
#             exercises.append(title)
#         else:
#             if title not in exercises:
#                 exercises.append(title)
#     token = input()
#
# i = 0
# while courses:
#     i += 1
#     print(f'{i}.{courses[0]}')
#     if courses[0] in exercises:
#         i += 1
#         exercises.remove(courses[0])
#         print(f'{i}.{courses[0]}-Exercise')
#     courses.remove(courses[0])


# # # More Exercises

# # 01. Social Distribution
# population = [int(x) for x in input().split(', ')]
# wealth = int(input())
# distribution_is_not_possible = False
# for i in range(len(population)):
#     max_wealth = max(population)
#     j = population.index(max(population))
#     difference = wealth - population[i]
#     if difference > 0 and (population[j] - difference >= wealth):
#         population[i] += difference
#         population[j] -= difference
#     elif difference <= 0:
#         continue
#     else:
#         distribution_is_not_possible = True
#         break
# if distribution_is_not_possible:
#     print('No equal distribution possible')
# else:
#     print(population)

# # 02. Take/Skip Rope
# line = list(input())
# numbers = [x for x in line if x.isdigit()]
# message = [x for x in line if x not in numbers]
# result = ''
# for i in range(len(numbers)):
#     j = int(numbers[i])
#     if i % 2 == 0:
#         if len(message) > j:
#             result += ''.join(message[:j])
#             message = message[j:]
#         else:
#             result += ''.join(message)
#             break
#     else:
#         if len(message) > j:
#             message = message[j:]
#         else:
#             break
# print(result)

# # 03. Kate's Way Out

# # 04. Battle Ships
# number = int(input())
# rows = []
# columns = []
# for i in range(number):
#     row = list(map(int, input().split()))
#     a = len(row)
#     rows.append(row)
# attacks = input().split()
# destroyed_ships = 0
# for attack in attacks:
#     attack = attack.split('-')
#     j = int(attack[0])
#     k = int(attack[1])
#     if rows[j][k] != 0:
#         rows[j][k] -= 1
#         if rows[j][k] == 0:
#             destroyed_ships += 1
# print(destroyed_ships)

# # 05. Dots