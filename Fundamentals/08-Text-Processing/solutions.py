# # # Lab
import re

# # 01. Reverse Strings
# word = input()
# while word != 'end':
#     reversed_word = word[::-1]
#     print(f'{word} = {reversed_word}')
#     word = input()

# # 02. Repeat Strings
# print(''.join([x * len(x) for x in input().split()]))

# # 03. Substring
# substring, text = input(), input()
# while substring in text:
#     text = text.replace(substring, '')
# print(text)

# # 04. Text Filter
# ban_list, text = input().split(', '), input()
# for word in ban_list:
#     while word in text:
#         text = text.replace(word, len(word) * '*')
# print(text)

# # 05. Digits, Letters and Other
# line = input()
# print(''.join([line[i] for i in range(len(line)) if line[i].isdigit()]))
# print(''.join([line[i] for i in range(len(line)) if line[i].isalpha()]))
# print(''.join([line[i] for i in range(len(line)) if not line[i].isalnum()]))


# # # Exercise

# # 01. Valid Usernames
# import re
#
# line = input().split(', ')
# regex = '^[a-zA-Z0-9_-]{3,16}$'
# print('\n'.join(x for x in line if re.match(regex, x)))

# # 02. Character Multiplier
# first, second = [list(x) for x in input().split(' ')]
# result = 0
# if len(second) > len(first):
#     first, second = second, first
# for i in range(len(first)):
#     if second:
#         result += ord(first[i]) * ord(second.pop(0))
#     else:
#         result += ord(first[i])
# print(result)

# # 03. Extract File
# path = input().split('\\')
# name, extension = path[-1].split('.')
# print(f'File name: {name}')
# print(f'File extension: {extension}')

# # 04. Caesar Cipher
# print(''.join([chr(ord(x) + 3) for x in list(input())]))

# # 05. Emoticon Finder
# text = input()
# [print(f":{text[i + 1]}") for i in range(len(text)) if text[i] == ':']

# # 06. Replace Repeating Chars
# line = input()
# result = [line[0]]
# for i in range(1, len(line)):
#     if line[i - 1] != line[i]:
#         result.append(line[i])
# print(''.join(result))

# # 07. String Explosion
# line, boom = input().split('>'), 0
# result = [line.pop(0)]
# for el in line:
#     el = list(el)
#     boom += (int(el.pop(0)) - 1)
#     while el and boom > 0:
#         el.pop(0)
#         boom -= 1
#     result.append(''.join(el))
# print('>'.join(result))

# # 08. Letters Change Numbers
# import re
#
# data, result = input(), 0
# line = re.findall('\\w{1}\\d+\\w{1}', data)
# for el in line:
#     alpha, beta = el[0], el[-1]
#     number = int(el[1:-1])
#     if alpha.isupper():
#         number /= (ord(alpha) - 64)
#     else:
#         number *= (ord(alpha) - 96)
#     if beta.isupper():
#         number -= (ord(beta) - 64)
#     else:
#         number += (ord(beta) - 96)
#     result += number
# print(f'{result:.2f}')

# # 09. Rage Quit
# import re
# line, element, unique = input(), '', []
# data = re.findall('\\D+\\d+', line)
# for el in data:
#     count = re.findall('\\d+', el)[0]
#     token = el[:-len(count)]
#     count = int(count)
#     unique.extend([x.upper() for x in token if x.upper() not in unique])
#     element += (''.join([x.upper() for x in token]) * count)
# print(f'Unique symbols used: {len(unique)}')
# print(element)

# 10. Winning Ticket
