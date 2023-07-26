# # # Lab


# # 01. Sum Matrix Elements
# rows, cols = [int(x) for x in input().split(', ')]
# matrix = [[int(i) for i in input().split(', ')] for row in range(rows)]
# print(sum([sum(row) for row in matrix]))
# print(matrix)

# # 02. Even Matrix
# rows = int(input())
# matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]
# print([[x for x in row if x % 2 == 0] for row in matrix])

# # 03. Flattening Matrix
# rows = int(input())
# matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]
# print([x for y in matrix for x in y])

# # 04. Sum Matrix Columns
# solution I
# rows, cols = [int(x) for x in input().split(', ')]
# matrix = [[int(x) for x in input().split(' ')] for row in range(rows)]
# for i in range(cols):
#     sum_column = 0
#     for j in range(rows):
#         sum_column += matrix[j][i]
#     print(sum_column)
# # solution II
# rows, cols = [int(x) for x in input().split(', ')]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# col_totals = [sum(x) for x in zip(*matrix)]
# print('\n'.join(str(x) for x in col_totals))

# # 05. Primary Diagonal
# size = int(input())
# matrix = [[int(x) for x in input().split(' ')] for row in range(size)]
# print(sum([matrix[i][i] for i in range(size)]))

# # 06. Symbol in Matrix
# # solution I
# size = int(input())
# matrix = [[x for x in list(input())] for row in range(size)]
# symbol, indices = input(), ''
# for c in range(size):
#     for r in range(size):
#         if matrix[r][c] == symbol:
#             indices = f'({r}, {c})'
#             break
# print(indices) if indices != '' else print(f'{symbol} does not occur in the matrix')
# # solution II
# size = int(input())
# matrix = [[x for x in input()] for _ in range(size)]
# symbol = input()
# result = [(index, row.index(symbol)) for index, row in enumerate(matrix) if symbol in row]
# print(result[0]) if result else print(f'{symbol} does not occur in the matrix')

# # 07. Square with Maximum Sum
# rows, cols = [int(x) for x in input().split(', ')]
# matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]
# sub_matrix, summary = [], 0
# for r in range(rows):
#     if r + 1 < rows:
#         for c in range(cols):
#             if c + 1 < cols:
#                 current_sum = matrix[r][c] + matrix[r + 1][c] + matrix[r][c + 1] + matrix[r + 1][c + 1]
#                 current_matrix = [[matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]]
#                 if current_sum > summary:
#                     summary = current_sum
#                     sub_matrix = current_matrix
# for el in sub_matrix:
#     print(' '.join(str(x) for x in el))
# print(summary)


# # # Exercise 1

# # 01. Diagonals
# size = int(input())
# matrix = [[int(x) for x in input().split(', ')] for row in range(size)]
# primary_diagonal = [matrix[i][i] for i in range(size)]
# sum_of_primary = sum(primary_diagonal)
# secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]
# sum_of_secondary = sum(secondary_diagonal)
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum_of_primary}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum_of_secondary}")

# # 02. Diagonal Difference
# size = int(input())
# matrix = [[int(x) for x in input().split(' ')] for row in range(size)]
# primary_diagonal = [matrix[i][i] for i in range(size)]
# secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]
# print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# # 03. 2x2 Squares in Matrix
# rows, cols = [int(x) for x in input().split(' ')]
# matrix = [[x for x in input().split(' ')] for row in range(rows)]
# count = 0
# for r in range(rows):
#     if r + 1 < rows:
#         for c in range(cols):
#             if c + 1 < cols:
#                 if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
#                     count += 1
# print(count)

# # 04. Maximal Sum
# rows, cols = [int(x) for x in input().split(' ')]
# matrix = [[int(x) for x in input().split(' ')] for row in range(rows)]
# max_sum, max_matrix = -9999, []
# for r in range(rows - 2):
#     for c in range(cols - 2):
#         current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + \
#                       matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2] + \
#                       matrix[r+2][c] + matrix[r+2][c+1] + matrix[r+2][c+2]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             max_matrix = [[matrix[r][c], matrix[r][c+1], matrix[r][c+2]],
#                           [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]],
#                           [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]]]
# print(f'Sum = {max_sum}')
# [print(*row) for row in max_matrix]

# # 05. Matrix of Palindromes
# # solution I
#
# rows, cols = [int(x) for x in input().split(' ')]
# matrix = []
# for r in range(rows):
#     row = []
#     for c in range(r, cols + r):
#         row.append(f'{chr(97 + r)}{chr(97 + c)}{chr(97 + r)}')
#     matrix.append(row)
# [print(*row) for row in matrix]
#
# # solution II
# rows, cols = [int(x) for x in input().split()]
# matrix = [['' for x in range(cols)] for _ in range(rows)]
# for row in range(rows):
#     for col in range(cols):
#         matrix[row][col] = chr(97 + row) + chr(97 + row + col) + chr(97 + row)
# [print(*row) for row in matrix]

# # 06. Matrix Shuffling
# def input_is_invalid(n, m, data):
#     if len(data) != 5 or data[0] != 'swap':
#         return True
#     r, c, r_1, c_1 = int(data[1]), int(data[2]), int(data[3]), int(data[4])
#     if r < 0 or r >= n or c < 0 or c >= m:
#         return True
#     if r_1 < 0 or r_1 >= n or c_1 < 0 or c_1 >= m:
#         return True
#     return False
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# command = input()
# while not command == 'END':
#     command = command.split()
#     if input_is_invalid(rows, cols, command):
#         print('Invalid input!')
#     else:
#         rw_1, cl_1, rw_2, cl_2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
#         matrix[rw_1][cl_1], matrix[rw_2][cl_2] = matrix[rw_2][cl_2], matrix[rw_1][cl_1]
#         [print(*row) for row in matrix]
#     command = input()

# # 07. Snake Moves
# rows, cols = [int(x) for x in input().split()]
# line = list(input())
# matrix = [['' for x in range(cols)] for _ in range(rows)]
# i = 0
# for r in range(rows):
#     if r % 2 == 0:
#         for c in range(cols):
#             matrix[r][c] = line[i]
#             i += 1
#             if i == len(line):
#                 i = 0
#     else:
#         for c in range(cols - 1, -1, -1):
#             matrix[r][c] = line[i]
#             i += 1
#             if i == len(line):
#                 i = 0
# [print(''.join(row)) for row in matrix]

# # 08. Bombs
# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# def get_neighbours(row, col, matrix):
#     size = len(matrix)
#     neighbours = []
#
#     # row - 1, col
#     if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
#         neighbours.append([row - 1, col])
#     # row + 1, col
#     if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
#         neighbours.append([row + 1, col])
#     # row, col - 1
#     if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
#         neighbours.append([row, col - 1])
#     # row, col + 1
#     if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
#         neighbours.append([row, col + 1])
#     # row - 1, col - 1
#     if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
#         neighbours.append([row - 1, col - 1])
#     # row - 1, col + 1
#     if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
#         neighbours.append([row - 1, col + 1])
#     # row + 1, col - 1
#     if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
#         neighbours.append([row + 1, col - 1])
#     # row + 1, col + 1
#     if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
#         neighbours.append([row + 1, col + 1])
#     return neighbours
#
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
#
# for bomb_coords in bombs:
#     bomb_row, bomb_col = [int(x) for x in bomb_coords.split(',')]
#
#     if matrix[bomb_row][bomb_col] <= 0:
#         continue
#
#     bomb_power = matrix[bomb_row][bomb_col]
#     matrix[bomb_row][bomb_col] = 0
#
#     for row, col in get_neighbours(bomb_row, bomb_col, matrix):
#         matrix[row][col] -= bomb_power
#
# alive_cells = 0
# alive_cells_sum = 0
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells += 1
#             alive_cells_sum += el
#
# print(f'Alive cells: {alive_cells}')
# print(f'Sum: {alive_cells_sum}')
#
# for row in matrix:
#     print(*row, sep=' ')

# # 09. Miner
# def direction_is_valid(r, c, n, direction, directions):
#     r += directions[direction][0]
#     c += directions[direction][1]
#     return 0 <= r < n and 0 <= c < n
#
#
# size = int(input())
# ways = [x for x in input().split()]
# matrix = [input().split() for _ in range(size)]
# row, col = 0, 0
# total_coals, coals = 0, 0
# for i in range(size):
#     for j in range(size):
#         if matrix[i][j] == 's':
#             row, col = i, j
#         elif matrix[i][j] == 'c':
#             total_coals += 1
# end_of_the_route = False
# info = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
# for way in ways:
#     if direction_is_valid(row, col, size, way, info):
#         matrix[row][col] = '*'
#         row += info[way][0]
#         col += info[way][1]
#         if matrix[row][col] == 'c':
#             coals += 1
#             if coals == total_coals:
#                 break
#         elif matrix[row][col] == 'e':
#             end_of_the_route = True
#             break
#         matrix[row][col] = '*'
# if coals == total_coals:
#     print(f'You collected all coal! ({row}, {col})')
# elif end_of_the_route:
#     print(f'Game over! ({row}, {col})')
# else:
#     print(f'{total_coals - coals} pieces of coal left. ({row}, {col})')

# # 10. Radioactive Mutate Vampire Bunnies
# def bunnies_update(rs, cs, field):
#     rabbits = []
#     for r in range(rs):
#         for c in range(cs):
#             if field[r][c] == 'B':
#                 rabbits.append([r, c])
#     return rabbits
#
#
# def explosion(rs, cs, rabbits, field):
#     for rabbit in rabbits:
#         r, c = rabbit[0], rabbit[1]
#         if 0 <= r - 1 and field[r - 1][c] != 'B':
#             field[r - 1][c] = 'B'
#         if r + 1 < rs and field[r + 1][c] != 'B':
#             field[r + 1][c] = 'B'
#         if 0 <= c - 1 and field[r][c - 1] != 'B':
#             field[r][c - 1] = 'B'
#         if c + 1 < cs and field[r][c + 1] != 'B':
#             field[r][c + 1] = 'B'
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [list(input()) for _ in range(rows)]
# directions = list(input())
# row, col = 0, 0
# bunnies = []
# for i in range(rows):
#     for j in range(cols):
#         if matrix[i][j] == 'P':
#             row, col = i, j
#         elif matrix[i][j] == 'B':
#             bunnies.append([i, j])
#
# ways = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
# player_won = False
# player_lost = False
#
# for way in directions:
#     matrix[row][col] = '.'
#     next_row = row + ways[way][0]
#     next_col = col + ways[way][1]
#     if 0 <= next_row < rows and 0 <= next_col < cols:
#         row, col = next_row, next_col
#         if matrix[row][col] == 'B':
#             player_lost = True
#             explosion(rows, cols, bunnies, matrix)
#         else:
#             matrix[row][col] = 'P'
#             explosion(rows, cols, bunnies, matrix)
#             bunnies = bunnies_update(rows, cols, matrix)
#             if matrix[row][col] == 'B':
#                 player_lost = True
#     else:
#         player_won = True
#         explosion(rows, cols, bunnies, matrix)
#     if player_won or player_lost:
#         break
#
# [print(''.join(row)) for row in matrix]
# if player_won:
#     print(f'won: {row} {col}')
# if player_lost:
#     print(f'dead: {row} {col}')


# # # Exercise 2

# # 01. Flatten Lists
# matrix = input().split('|')
# matrix = [matrix[i].split() for i in range(len(matrix))][::-1]
# flatten_list = [j for sub in matrix for j in sub]
# print(*flatten_list)

# # 02. Matrix Modification
# size = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(size)]
# info = input().split()
# while not info[0] == 'END':
#     row, col, value = [int(x) for x in info[1:]]
#     data = {'Add': [row, col, value], 'Subtract': [row, col, -value]}
#     if 0 <= row < size and 0 <= col < size:
#         matrix[row][col] += data[info[0]][2]
#     else:
#         print('Invalid coordinates')
#     info = input().split()
# [print(*row) for row in matrix]

# # 03. Knight Game
# def fights_counter(rw, cl, turns):
#     counter = 0
#     for turn in turns:
#         r = rw + turns[turn][0]
#         c = cl + turns[turn][1]
#         if 0 <= r < size and 0 <= c < size and matrix[r][c] == 'K':
#             counter += 1
#     return counter
#
#
# size = int(input())
# matrix = [list(input()) for _ in range(size)]
# knights = [[x, y] for x in range(size) for y in range(size) if matrix[x][y] == 'K']
# moves = {'1': [-1, -2], '2': [-2, -1], '3': [-2, 1], '4': [-1, 2],
#          '5': [1, 2], '6': [2, 1], '7': [2, -1], '8': [1, -2]}
# removed_knights = 0
# no_detection = False
#
# while True:
#     max_fights = 0
#     knights_to_remove = []
#     for knight in knights:
#         row, col = knight[0], knight[1]
#         result = fights_counter(row, col, moves)
#         if result > max_fights:
#             max_fights = result
#             knights_to_remove = [row, col]
#     if max_fights != 0:
#         i = knights.index(knights_to_remove)
#         matrix[knights_to_remove[0]][knights_to_remove[1]] = '0'
#         del knights[i]
#         removed_knights += 1
#     else:
#         no_detection = True
#         break
# print(removed_knights)

# # 04. Easter Bunny
# size = int(input())
# matrix = [input().split() for _ in range(size)]
# bunny = [(r, c) for r in range(size) for c in range(size) if matrix[r][c] == 'B']
# row, col = bunny[0][0], bunny[0][1]
# ways = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
# result = ['', [], 0]
#
# for way in ways:
#     r, c, eggs, steps = row, col, 0, []
#     while True:
#         r += ways[way][0]
#         c += ways[way][1]
#         if 0 <= r < size and 0 <= c < size and matrix[r][c] != 'X':
#             eggs += int(matrix[r][c])
#             steps.append([r, c])
#         else:
#             break
#     if eggs >= result[2]:
#         result[0], result[1], result[2] = way, steps, eggs
#
# print(f"{result[0]}")
# [print(step) for step in result[1]]
# print(f"{result[2]}")

# # 05. Alice in Wonderland
# size = int(input())
# matrix = [input().split() for _ in range(size)]
# alice = [[x, y] for x in range(size) for y in range(size) if matrix[x][y] == 'A']
# row, col = alice[0][0], alice[0][1]
# tea_bags = 0
# moves = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
# move = input()
# while tea_bags < 10:
#     matrix[row][col] = '*'
#     row += moves[move][0]
#     col += moves[move][1]
#     if 0 <= row < size and 0 <= col < size:
#         if matrix[row][col].isdigit():
#             tea_bags += int(matrix[row][col])
#             if tea_bags >= 10:
#                 matrix[row][col] = '*'
#                 break
#         elif matrix[row][col] == 'R':
#             matrix[row][col] = '*'
#             break
#         else:
#             matrix[row][col] = 'A'
#     else:
#         break
#     move = input()
# if tea_bags >= 10:
#     print('She did it! She went to the party.')
# else:
#     print("Alice didn't make it to the tea party.")
# [print(*row) for row in matrix]

# # 06. Range Day
# size = 5
# matrix = [input().split() for _ in range(size)]
# shooter = [[x, y] for x in range(size) for y in range(size) if matrix[x][y] == 'A']
# row, col = shooter[0][0], shooter[0][1]
# targets = sum(i.count('x') for i in matrix)
# ways = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
# hit_targets = []
#
# number_of_commands = int(input())
# for _ in range(number_of_commands):
#     command = input().split()
#     if command[0] == 'shoot':
#         r, c = row, col
#         way = command[1]
#         while True:
#             r += ways[way][0]
#             c += ways[way][1]
#             if not 0 <= r < size or not 0 <= c < size:
#                 break
#             if matrix[r][c] == 'x':
#                 hit_targets.append([r, c])
#                 targets -= 1
#                 matrix[r][c] = '.'
#                 break
#         if targets == 0:
#             break
#     else:
#         way, steps = command[1], int(command[2])
#         step_dict = {'up': (row - steps, col), 'down': (row + steps, col),
#                      'left': (row, col - steps), 'right': (row, col + steps)}
#         r, c = step_dict[way][0], step_dict[way][1]
#         if 0 <= r < size and 0 <= c < size and matrix[r][c] == '.':
#             matrix[row][col] = '.'
#             row, col = r, c
#             matrix[row][col] = 'A'
#
# if targets == 0:
#     print(f'Training completed! All {len(hit_targets)} targets hit.')
# else:
#     print(f'Training not completed! {targets} targets left.')
# [print(target) for target in hit_targets]

# # 07. Present Delivery
# presents, size = int(input()), int(input())
# matrix = [input().split() for _ in range(size)]
# santa = [[x, y] for x in range(size) for y in range(size) if matrix[x][y] == 'S']
# row, col = santa[0][0], santa[0][1]
# nice_kids = sum(i.count('V') for i in matrix)
# ways = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
# nice_kids_remaining = nice_kids
# no_more_presents = False
#
# way = input()
# while way != 'Christmas morning':
#     matrix[row][col] = '-'
#     row += ways[way][0]
#     col += ways[way][1]
#     if matrix[row][col] == 'V':
#         matrix[row][col] = 'S'
#         presents -= 1
#         nice_kids_remaining -= 1
#         if presents == 0:
#             break
#     elif matrix[row][col] == 'C':
#         matrix[row][col] = 'S'
#         for key in ways:
#             r = row + ways[key][0]
#             c = col + ways[key][1]
#             if matrix[r][c].isalpha():
#                 presents -= 1
#                 if matrix[r][c] == 'V':
#                     nice_kids_remaining -= 1
#                 matrix[r][c] = '-'
#                 if presents == 0:
#                     no_more_presents = True
#                     break
#     else:
#         matrix[row][col] = 'S'
#     if no_more_presents:
#         break
#     way = input()
#
# if presents == 0 and nice_kids_remaining > 0:
#     print('Santa ran out of presents!')
# [print(*row) for row in matrix]
# if nice_kids_remaining == 0:
#     print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
# else:
#     print(f'No presents for {nice_kids_remaining} nice kid/s.')