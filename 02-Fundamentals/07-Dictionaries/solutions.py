# # # Lab

# # 01. Bakery
# line = input().split(' ')
# print({line[i - 1]: int(line[i]) for i in range(1, len(line), 2)})

# # 02. Stock
# line = input().split(' ')
# products = input().split(' ')
# stock = {line[i - 1]: int(line[i]) for i in range(1, len(line), 2)}
# for product in products:
#     if product in stock.keys():
#         print(f'We have {stock[product]} of {product} left')
#     else:
#         print(f"Sorry, we don't have {product}")

# # 03. Statistics
# products = {}
# data = input()
# while data != 'statistics':
#     line = data.split(': ')
#     if line[0] not in products:
#         products[line[0]] = 0
#     products[line[0]] += int(line[1])
#     data = input()
# result = ['Products in stock:']
# for product in products:
#     result.append(f'- {product}: {products[product]}')
# result.append(f'Total Products: {len(products)}')
# result.append(f'Total Quantity: {sum(x for x in products.values())}')
# print('\n'.join(result))

# # 04. Students
# courses = {}
# line = input()
# while ':' in line:
#     data = line.split(':')
#     course = '_'.join(data[2].split(' '))
#     if course not in courses:
#         courses[course] = {}
#     courses[course][data[0]] = data[1]
#     line = input()
# course = line
# for student, student_id in courses[course].items():
#     print(f'{student} - {student_id}')

# # 05. ASCII Values
# line = input().split(', ')
# result = {}
# for el in line:
#     if el not in result:
#         result[el] = ord(el)
# print(result)

# # 06. Odd Occurrences
# line = [x.lower() for x in input().split(' ')]
# dictionary, result = {}, []
# for el in line:
#     if el not in dictionary:
#         dictionary[el] = 0
#     dictionary[el] += 1
# for k, v in dictionary.items():
#     if v % 2 != 0:
#         result.append(k)
# print(' '.join(result))

# # 07. Word Synonyms
# number = int(input()) * 2
# synonyms = {}
# words = [input() for x in range(number)]
# for i in range(0, len(words) - 1, 2):
#     if words[i] not in synonyms:
#         synonyms[words[i]] = []
#     synonyms[words[i]].append(words[i + 1])
# for word in synonyms:
#     print(f"{word} - {', '.join(synonyms[word])}")


# # # Exercise

# # 01. Count Chars in a String
# line = [x for x in list(input()) if x != ' ']
# result = {}
# for i in range(len(line)):
#     if line[i] not in result:
#         result[line[i]] = 0
#     result[line[i]] += 1
# for k, v in result.items():
#     print(f'{k} -> {v}')

# # 02. A Miner Task
# resources = {}
# info = input()
# while info != 'stop':
#     if info not in resources:
#         resources[info] = 0
#     resources[info] += int(input())
#     info = input()
# for k, v in resources.items():
#     print(f'{k} -> {v}')

# # 03. Capitals
# countries, capitals = input().split(', '), input().split(', ')
# result = {countries[i]: capitals[i] for i in range(len(countries))}
# for country, capital in result.items():
#     print(f'{country} -> {capital}')

# # 04. Phonebook
# phonebook = {}
# data = input()
# while not data.isdigit():
#     person, phone = data.split('-')
#     phonebook[person] = phone
#     data = input()
# for p in range(int(data)):
#     name = input()
#     if name in phonebook:
#         print(f'{name} -> {phonebook[name]}')
#     else:
#         print(f'Contact {name} does not exist.')

# # 05. Legendary Farming
# items = {'shards': 'Shadowmourne',
#          'fragments': 'Valanyr',
#          'motes': 'Dragonwrath'}
# points = 250
# legendary_obtained = False
# final = {'shards': 0, 'fragments': 0, 'motes': 0}
# legendary_items = ['shards', 'fragments', 'motes']
# materials = input().split(' ')
#
# while True:
#     for i in range(1, len(materials), 2):
#         quantity = int(materials[i - 1])
#         material = materials[i].lower()
#         if material not in final:
#             final[material] = 0
#         final[material] += quantity
#         if material in legendary_items and final[material] >= points:
#             print(f'{items[material]} obtained!')
#             final[material] -= points
#             legendary_obtained = True
#             break
#     if legendary_obtained:
#         break
#     else:
#         materials = input().split(' ')
# for k, v in final.items():
#     print(f'{k}: {v}')

# # Orders
# products = {}
# data = input().split(' ')
# while data[0] != 'buy':
#     product, price, quantity = data[0], float(data[1]), int(data[2])
#     if product not in products:
#         products[product] = [0, 0.0]
#     products[product][0] = price
#     products[product][1] += quantity
#     data = input().split(' ')
# for k, v in products.items():
#     print(f'{k} -> {(v[0] * v[1]):.2f}')

# # 07. SoftUni Parking
# n, lot = int(input()), {}
# for i in range(n):
#     data = input().split(' ')
#     command, username = data[0], data[1]
#     if command == 'register':
#         license_plate_number = data[2]
#         if username in lot and lot[username]:
#             print(f'ERROR: already registered with plate number {license_plate_number}')
#         else:
#             lot[username] = license_plate_number
#             print(f'{username} registered {license_plate_number} successfully')
#     else:
#         if username not in lot:
#             print(f'ERROR: user {username} not found')
#         else:
#             del lot[username]
#             print(f'{username} unregistered successfully')
# for k, v in lot.items():
#     print(f'{k} => {v}')

# # 08. Courses
# courses = {}
# data = input()
# while data != 'end':
#     course_name, student_name = data.split(' : ')
#     if course_name not in courses:
#         courses[course_name] = []
#     courses[course_name].append(student_name)
#     data = input()
# for k, v in courses.items():
#     print(f'{k}: {len(v)}')
#     for s in v:
#         print(f'-- {s}')

# # 09. Student Academy
# students = {}
# n = int(input())
# for i in range(n):
#     student, grade = input(), float(input())
#     if student not in students:
#         students[student] = []
#     students[student].append(grade)
# for k, v in students.items():
#     average_grade = sum(v) / len(v)
#     if average_grade >= 4.50:
#         print(f'{k} -> {average_grade:.2f}')

# # 10. Company Users
# result = {}
# data = input()
# while data != 'End':
#     company, employee_id = data.split(' -> ')
#     if company not in result:
#         result[company] = []
#     if employee_id not in result[company]:
#         result[company].append(employee_id)
#     data = input()
# for company_name, employees in result.items():
#     print(company_name)
#     for employee in employees:
#         print(f'-- {employee}')

# # 11. Force Book
# sides, users = {}, []
# data = input()
# while data != 'Lumpawaroo':
#     if ' | ' in data:
#         side, user = data.split(' | ')
#         if user not in users and side not in sides:
#             sides[side] = [user]
#             users.append(user)
#         elif user not in users and side in sides:
#             sides[side].append(user)
#             users.append(user)
#     elif ' -> ' in data:
#         user, side = data.split(' -> ')
#         if user in users:
#             for force_side in sides:
#                 if user in sides[force_side]:
#                     sides[force_side] = [x for x in sides[force_side] if x != user]
#             if side not in sides:
#                 sides[side] = []
#             sides[side].append(user)
#         elif user not in users and side in sides:
#             sides[side].append(user)
#         elif user not in users and side not in sides:
#             sides[side] = [user]
#         print(f'{user} joins the {side} side!')
#     data = input()
# for s, u in sides.items():
#     if u:
#         print(f'Side: {s}, Members: {len(u)}')
#         for gamer in u:
#             print(f'! {gamer}')

# # 12. SoftUni Exam Results
# info = input()
# submissions = {}
#
# while info != 'exam finished':
#     data = info.split('-')
#     if 'banned' in data:
#         student = data[0]
#         for discipline in submissions:
#             if submissions:
#                 if student in submissions[discipline][1]:
#                     del submissions[discipline][1][student]
#     else:
#         student, language, points = data[0], data[1], int(data[2])
#         if language not in submissions:
#             submissions[language] = [0, {}]
#         submissions[language][0] += 1
#         if student not in submissions[language][1]:
#             submissions[language][1][student] = int(points)
#         else:
#             if submissions[language][1][student] < points:
#                 submissions[language][1][student] = points
#     info = input()
# print('Results:')
# for exam in submissions:
#     for student, result in submissions[exam][1].items():
#         print(f'{student} | {result}')
# print('Submissions:')
# for language in submissions:
#     print(f'{language} - {submissions[language][0]}')


# # # More Exercises

# # 01. Ranking
# contests = {}
# data = input()
# while data != 'end of contests':
#     c, p = data.split(':')
#     contests[c] = p
#     data = input()
# users = {}
# line = input()
# while line != 'end of submissions':
#     contest, password, user, points = line.split('=>')
#     points = int(points)
#     if contest in contests and contests[contest] == password:
#         if user not in users:
#             users[user] = {contest: points}
#         elif user in users and contest not in users[user]:
#             users[user][contest] = points
#         if user in users and contest in users[user] and points > users[user][contest]:
#             users[user][contest] = points
#     line = input()
# best_candidate, best_score = '', 0
# for candidate, result in users.items():
#     total_points = sum(result.values())
#     if total_points > best_score:
#         best_candidate = candidate
#         best_score = total_points
# sorted_users = {k: v for k, v in sorted(users.items(), key=lambda item: item[0])}
# final = {}
# for k, v in sorted_users.items():
#     sorted_users[k] = {i: j for i, j in sorted(v.items(), key=lambda item: -item[1])}
#
# print(f'Best candidate is {best_candidate} with total {best_score} points.')
# print('Ranking:')
# for k, v in sorted_users.items():
#     print(k)
#     for d, p in v.items():
#         print(f'#  {d} -> {p}')

# # 02. Judge
# contests = {}
# line = input()
# while line != 'no more time':
#     user, contest, points = line.split(' -> ')
#     points = int(points)
#     if contest not in contests:
#         contests[contest] = {}
#     if user not in contests[contest]:
#         contests[contest][user] = points
#     else:
#         if points > contests[contest][user]:
#             contests[contest][user] = points
#     line = input()
# users = {}
# for c, s in contests.items():
#     contests[c] = {k: v for k, v in sorted(s.items(), key=lambda x: (-x[1], x[0]))}
# for exam, students in contests.items():
#     for student in students:
#         if student not in users:
#             users[student] = 0
#         users[student] += students[student]
# sorted_users = {k: v for k, v in sorted(users.items(), key=lambda i: (-i[1], i[0]))}
# for k, v in contests.items():
#     print(f'{k}: {len(v)} participants')
#     i = 0
#     for x, y in v.items():
#         i += 1
#         print(f'{i}. {x} <::> {y}')
# print('Individual standings:')
# j = 0
# for a, b in sorted_users.items():
#     j += 1
#     print(f'{j}. {a} -> {b}')

# # 03. MOBA Challenger
# pool = {}
# token = input()
# while token != 'Season end':
#     if ' -> ' in token:
#         line = token.split(' -> ')
#         player, position, skill = line[0], line[1], int(line[2])
#         if player not in pool:
#             pool[player] = {position: skill}
#         else:
#             if position not in pool[player] or skill > pool[player][position]:
#                 pool[player][position] = skill
#     elif ' vs ' in token:
#         pl_one, pl_two = token.split(' vs ')
#         if pl_one in pool and pl_two in pool:
#             for skill in pool[pl_one]:
#                 if skill in pool[pl_two]:
#                     t_one = sum(pool[pl_one].values())
#                     t_two = sum(pool[pl_two].values())
#                     if t_one > t_two:
#                         del pool[pl_two]
#                     elif t_two > t_one:
#                         del pool[pl_one]
#                     break
#     token = input()
# for name, skills in sorted(pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
#     print(f'{name}: {sum(skills.values())} skill')
#     for p, s in sorted(skills.items(), key=lambda x: (-x[1], x[0])):
#         print(f'- {p} <::> {s}')

# # 04. Snow White
# dwarves = {}
# dwarves_info = []
#
# hat_len = 'hat len'
# d_name = 'name'
# d_physics = 'physics'
# d_hat = 'hat'
#
# dwarf = input()
# while dwarf != 'Once upon a time':
#     name, color, physics = [int(x) if x.isdigit() else x for x in dwarf.split(' <:> ')]
#     if color not in dwarves:
#         dwarves[color] = {}
#     if name not in dwarves[color]:
#         dwarves[color][name] = 0
#     if dwarves[color][name] < physics:
#         dwarves[color][name] = physics
#
#     dwarf = input()
#
# for color in dwarves:
#     for name, points in dwarves[color].items():
#         dwarves_info.append({hat_len: len(dwarves[color]), d_name: name, d_physics: points, d_hat: color})
# for s_dwarf in sorted(dwarves_info, key=lambda x: (-x[d_physics], -x[hat_len])):
#     print(f'({s_dwarf[d_hat]}) {s_dwarf[d_name]} <-> {s_dwarf[d_physics]}')

# # 05. Dragon Army
# number, dragons = int(input()), {}
# default_values = {'health': 250, 'damage': 45, 'armor': 10}
# for i in range(number):
#     type, name, damage, health, armor = input().split(' ')
#     damage = default_values['damage'] if not damage.isdigit() or damage == 0 else int(damage)
#     health = default_values['health'] if not health.isdigit() or health == 0 else int(health)
#     armor = default_values['armor'] if not armor.isdigit() or armor == 0 else int(armor)
#     if type not in dragons:
#         dragons[type] = {name: {'damage': damage, 'health': health, 'armor': armor}}
#     dragons[type][name] = {'damage': damage, 'health': health, 'armor': armor}
#
# for dragon_type in dragons:
#     dragons[dragon_type] = {k: v for k, v in sorted(dragons[dragon_type].items(), key=lambda x: x[0])}
#     a_damage, a_health, a_armor, dragons_data = 0, 0, 0, []
#     for dragon in dragons[dragon_type]:
#         a_damage += dragons[dragon_type][dragon]['damage']
#         a_health += dragons[dragon_type][dragon]['health']
#         a_armor += dragons[dragon_type][dragon]['armor']
#         dragons_data.append(f"-{dragon} -> damage: {dragons[dragon_type][dragon]['damage']}, "
#                             f"health: {dragons[dragon_type][dragon]['health']}, "
#                             f"armor: {dragons[dragon_type][dragon]['armor']}")
#     a_damage /= len(dragons[dragon_type])
#     a_health /= len(dragons[dragon_type])
#     a_armor /= len(dragons[dragon_type])
#     print(f'{dragon_type}::({a_damage:.2f}/{a_health:.2f}/{a_armor:.2f})')
#     print('\n'.join(dragons_data))