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
