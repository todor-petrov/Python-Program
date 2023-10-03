# # 01. File Opener
# import os

# try:
#     file = open('text.txt')
#     print('File found')
# except FileNotFoundError:
#     print('File not found')

# if os.path.exists('text.txt'):
#     print('File found')
# else:
#     print('File not found')


# # 02. File Reader
# try:
#     with open('numbers.txt', 'r') as file:
#         print(sum(int(line) for line in file.readlines()))
# except FileNotFoundError:
#     print('File not found')


# # 03. File Writer
# with open('my_first_file.txt', 'a') as file:
#     file.writelines('I just created my first file!')


# # 04. File Delete
# import os
#
# try:
#     os.remove('my_first_file.txt')
# except FileNotFoundError:
#     print('File already deleted!')
#
# if os.path.exists('my_first_file.txt'):
#     os.remove('my_first_file.txt')
# else:
#     print('File already deleted!')


# # 05. Word count
# import re
#
#
# def read_searched_words(file_path):
#     searched_words = []
#     with open(file_path) as file:
#         searched_words = file.read().split()
#     return searched_words
#
#
# def calculate_words_count(searched_words, file_path):
#     words_count = {}
#     with open(file_path) as file:
#         text = file.read()
#         for word in searched_words:
#             pattern = fr'\b{word}\b'
#             count = len(re.findall(pattern, text, re.IGNORECASE))
#             words_count[word] = count
#     return words_count
#
#
# def store_result(result, output_file_path):
#     with open(output_file_path, 'w') as file:
#         sorted_result = sorted(result.items(), key=lambda kvp: -kvp[1])
#         for key, value in sorted_result:
#             file.writelines(f'{key} - {value}\n')
#
#
# words = read_searched_words('words.txt')
# result = calculate_words_count(words, 'input.txt')
# store_result(result, 'output.txt')
