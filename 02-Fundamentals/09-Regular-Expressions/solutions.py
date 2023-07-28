# # # Lab


# # 01. Match Full Name
# import re
#
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# text = input()
# valid_names = re.findall(pattern, text)
# print(" ".join(valid_names))

# # 02. Match Phone Number
# import re
#
# pattern = r'\+359(\s|-)2(\1)\d{3}(\1)\d{4}\b'
# line = input()
# print(', '.join([match.group() for match in re.finditer(pattern, line)]))

# # 03. Match Dates
# import re
#
# pattern = r'(?P<day>\d{2})(/|\.|-)(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})'
# line = input()
# days = [match.groupdict() for match in re.finditer(pattern, line)]
# for element in days:
#     print(f"Day: {element['day']}, Month: {element['month']}, Year: {element['year']}")

# # 04. Match Numbers
# import re
#
# pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
# line = input()
# print(' '.join([match.group() for match in re.finditer(pattern, line)]))


# # # Exercise

# # 01. Capture the Numbers
# import re
#
# line, result = input(), []
# while line:
#     result.extend(re.findall('\\d+', line))
#     line = input()
# print(' '.join(result))

# # 02. Find Variable Names in Sentences
# import re
#
# line = input()
# pattern = '\\b_{1}([a-zA-Z0-9]+\\b)'
# print(','.join(re.findall(pattern, line)))

# # 03. Find Occurrences of Word in Sentence
# import re
#
# line, word = input().lower(), input().lower()
# print(len(re.findall(f'\\b{word}\\b', line)))

# # 04. Extract Emails
# import re
#
# text = input()
# regex = '((?<=\\s)[a-zA-Z0-9]+([-.]\\w*)*@[a-zA-Z]+?([.-][a-zA-Z]*)*(\\.[a-z]{2,}))'
# result = re.findall(regex, text)
# for element in result:
#     print(element[0])

# # 05. Furniture
# import re
#
# pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)"
# text = input()
# total = 0
# furniture_name = []
# while not text == 'Purchase':
#
#     match = re.findall(pattern, text)
#     if match:
#         for i in match:
#             furniture_name.append(i[0])
#
#             price = float(i[1])
#             quantity = float(i[2])
#             total += price * quantity
#
#     text = input()
# print('Bought furniture:')
# for i in furniture_name:
#     print(i)
# print(f'Total money spend: ' + "{:.2f}".format(total))

# # 06. Extract the Links
# import re
#
# text = input()
# while text:
#     result = re.findall('www.[a-zA-Z0-9\\-]+\\.[a-z\\.]+', text)
#     if result:
#         print('\n'.join(result))
#     text = input()


# # # More Exercises

# # 01. Race
# import re
#
# participants = input().split(', ')
# line = input()
# final = {}
# while line != 'end of race':
#     name_pattern = r'[a-zA-Z]+'
#     distance_pattern = r'\d'
#     name = ''.join([match for match in re.findall(name_pattern, line)])
#     distance = sum([int(match) for match in re.findall(distance_pattern, line)])
#     if name in participants:
#         if name not in final:
#             final[name] = 0
#         final[name] += distance
#     line = input()
# final = sorted(final.items(), key=lambda x: -x[1])
# count = 0
# for el in final:
#     count += 1
#     if count == 1:
#         print(f'1st place: {el[0]}')
#     elif count == 2:
#         print(f'2nd place: {el[0]}')
#     else:
#         print(f'3rd place: {el[0]}')
#         break

# # 02. SoftUni Bar Income
# import re
#
# pattern = r'%(?P<name>[A-Z][a-z]+)%[^\|\$%\.]*?\<(?P<product>\w+)\>[^\|\$\%\.]*?\|(?P<count>\d+)\|[^\|\$\%\.]*?(?P<price>\d+\.?\d+)\$'
# info = input()
# total_income = 0
# while info != 'end of shift':
#     matches = [match.groups() for match in re.finditer(pattern, info)]
#     if matches:
#         student, product = matches[0][0], matches[0][1]
#         money_spent = int(matches[0][2]) * float(matches[0][3])
#         print(f'{student}: {product} - {money_spent:.2f}')
#         total_income += money_spent
#     info = input()
# if total_income > 0:
#     print(f'Total income: {total_income:.2f}')

# # 03. Star Enigma
# import re
#
# count_pattern = r'[star]'
# integer = int(input())
# attacked_planets, destroyed_planets = [], []
# for _ in range(integer):
#     encrypted = input()
#     count = len(re.findall(count_pattern, encrypted, re.I))
#     decrypted = ''.join([chr(ord(encrypted[i]) - count) for i in range(len(encrypted))])
#     pattern = r'@(?P<planet>[a-zA-Z]+)[^@\-\!\:\>]*?' \
#               r':(?P<population>\d+)[^@\-\!\:\>]*?' \
#               r'\!(?P<type>[AD])\![^@\-\!\:\>]*?' \
#               r'\-\>(?P<soldiers>\d+)'
#     matches = [match.groups() for match in re.finditer(pattern, decrypted)]
#     if matches:
#         if matches[0][2] == 'A':
#             attacked_planets.append(matches[0][0])
#         else:
#             destroyed_planets.append(matches[0][0])
# print(f'Attacked planets: {len(attacked_planets)}')
# if attacked_planets:
#     for planet in sorted(attacked_planets):
#         print(f'-> {planet}')
# print(f'Destroyed planets: {len(destroyed_planets)}')
# if destroyed_planets:
#     for planet in sorted(destroyed_planets):
#         print(f'-> {planet}')

# # 04. Nether Realms
# import re
#
# pattern_health = r'[^0-9\+\-\*\/\.]'
# pattern_damage = r'(-?\d+(\.\d+)?)'
# line = [el.strip() for el in input().split(',')]
# demon_health = 0
# damage = 0
#
# for name in sorted(line):
#
#     matches_health = re.findall(pattern_health, name)
#     matches_damage = re.findall(pattern_damage, name)
#     for match in matches_health:
#         if match:
#             demon_health += ord(match)
#     for el in matches_damage:
#         if el:
#             damage += float(el[0])
#     for char in name:
#         if char == '*':
#             damage *= 2
#         elif char == '/':
#             damage /= 2
#     print(f'{name} - {demon_health} health, {damage:.2f} damage')
#     demon_health = 0
#     damage = 0

# # 05. HTML Parser
# import re
#
# pattern = r'\<title\>(?P<title>.*)\<\/title\>.*\<body>(?P<content>.*)\<\/body\>'
# junk_pattern = r'\<[^\<]+\>|\\n'
# line = input()
# title = ''.join([match.group('title') for match in re.finditer(pattern, line)])
# content = ''.join([match.group('content') for match in re.finditer(pattern, line)])
# junk = [match.group() for match in re.finditer(junk_pattern, content)]
# for el in junk:
#     if el in content:
#         content = content.replace(el, '', 1)
# print(f'Title: {title}')
# print(f'Content: {content}')