# # 01. Even Lines
# symbols = ['-', ',', '.', '!', '?']
# with open('text.txt', 'r') as even_lines_file:
#     text = even_lines_file.readlines()
# for row in range(0, len(text), 2):
#     for symbol in symbols:
#         text[row] = text[row].replace(symbol, '@')
#
#     print(*text[row].split()[::-1])


# # 02. Line Numbers
# from string import punctuation
#
# output_file = open('output.txt', 'a')
# with open('text.txt', 'r') as text_file:
#     text = text_file.readlines()
#
# for i in range(len(text)):
#     row = text[i]
#
#     letters, marks = 0, 0
#
#     for symbol in row:
#         if symbol.isalpha():
#             letters += 1
#         elif symbol in punctuation:
#             marks += 1
#
#     output_file.write(f"Line: {i+1}: {''.join(row[:-1])} ({letters})({marks})\n")
#
# output_file.close()


# # 03. File Manipulator
# import os
#
# while True:
#     info = input().split('-')
#
#     if info[0] == 'Create':
#         file = open(f'{info[1]}', 'w')
#         file.close()
#
#     elif info[0] == 'Add':
#         with open(f'{info[1]}', 'a') as file:
#             file.write(f'{info[2]}\n')
#
#     elif info[0] == 'Replace':
#         try:
#             with open(f'{info[1]}', 'r') as file:
#                 text = file.readlines()
#
#             file = open(f'{info[1]}', 'w')
#             for i in range(len(text)):
#                 text[i] = text[i].replace(info[2], info[3])
#             file.write(''.join(text))
#             file.close()
#
#         except FileNotFoundError:
#             print('An error occurred')
#
#     elif info[0] == 'Delete':
#         try:
#             os.remove(f'{info[1]}')
#         except FileNotFoundError:
#             print('An error occurred')
#
#     else:
#         break
