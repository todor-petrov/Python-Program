# # # Lab


# # 01. Reverse String
# print(input()[::-1])

# # 02. Matching Parentheses
# line = input()
# brackets = []
# for i in range(len(line)):
#     if line[i] == '(':
#         brackets.append(i)
#     elif line[i] == ')':
#         j = brackets.pop()
#         print(line[j:(i + 1)])

# # 03. Supermarket
# token, queue = input(), []
# while not token == 'End':
#     if token == 'Paid' and queue:
#         print('\n'.join(queue))
#         queue = []
#     else:
#         queue.append(token)
#     token = input()
# print(f'{len(queue)} people remaining.')

# # 04. Water Dispenser
# from collections import deque
#
# dispenser, name, people = int(input()), input(), deque()
# while name != 'Start':
#     people.append(name)
#     name = input()
# command = input()
# while not command == 'End':
#     if 'refill' in command:
#         command = command.split(' ')
#         dispenser += int(command[1])
#     else:
#         if int(command) <= dispenser:
#             dispenser -= int(command)
#             print(f'{people.popleft()} got water')
#         else:
#             print(f'{people.popleft()} must wait')
#     command = input()
# print(f'{dispenser} liters left')

# # 05. Hot Potato
# from collections import deque
# kids, toss = deque(input().split(' ')), int(input())
# while len(kids) > 1:
#     for i in range(toss):
#         kids.append(kids.popleft())
#     print(f'Removed {kids.pop()}')
# print(f'Last is {kids.popleft()}')


# # # Exercise

# # 01. Reverse Numbers
# numbers = [int(x) for x in input().split()]
# while numbers:
#     print(numbers.pop(), end=' ')

# # 02. Stacked Queries
# number = int(input())
# stack = []
# for _ in range(number):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         stack.append(query[1])
#     elif query[0] == 2 and stack:
#         stack.pop()
#     elif query[0] == 3 and stack:
#         print(max(stack))
#     elif query[0] == 4 and stack:
#         print(min(stack))
# while stack:
#     if len(stack) == 1:
#         print(stack.pop())
#     else:
#         print(stack.pop(), end=', ')

# # 03. Fast Food
# from collections import deque
#
# quantity = int(input())
# orders = deque([int(x) for x in input().split()])
# print(max(orders))
# while orders:
#     if quantity >= orders[0]:
#         quantity -= orders.popleft()
#     else:
#         break
# if orders:
#     print(f"Orders left: {' '.join(str(x) for x in orders)}")
# else:
#     print('Orders complete')

# # 04. Fashion Boutique
# clothes = [int(x) for x in input().split()]
# rack_capacity = int(input())
# racks_counter = 1
# rack = rack_capacity
# while clothes:
#     if clothes[-1] <= rack:
#         rack -= clothes.pop()
#     else:
#         racks_counter += 1
#         rack = rack_capacity
#         rack -= clothes.pop()
# print(racks_counter)

# # 05. Truck Tour
# from collections import deque
#
# number = int(input())
# pumps = deque()
# for pump in range(number):
#     pumps.append([int(x) for x in input().split()])
# pump_number = 0
#
# for turn in range(number):
#     turn_is_successful = True
#     pump_number = turn
#     fuel = 0
#     for pump in pumps:
#         fuel += pump[0]
#         distance = pump[1]
#         fuel -= distance
#         if fuel < 0:
#             pumps.append(pumps.popleft())
#             turn_is_successful = False
#             break
#     if turn_is_successful:
#         break
# print(pump_number)

# # 06. Balanced Parentheses
# from collections import deque
#
# line = deque(input())
# result = deque()
# my_list = ['()', '[]', '{}']
# while line:
#     result.append(line.popleft())
#     if len(result) > 1 and result[-2] + result[-1] in my_list:
#         result.pop(), result.pop()
# print('NO') if result else print('YES')

# # 07. Robotics
# from collections import deque
#
#
# def convert_str_to_seconds(str_time):
#     hours, minutes, seconds = [int(x) for x in str_time.split(':')]
#     return hours * 60 * 60 + minutes * 60 + seconds
#
#
# def convert_seconds_to_str_time(seconds):
#     seconds %= 24 * 60 * 60
#     hours = seconds // (60 * 60)
#     seconds %= (60 * 60)
#     minutes = seconds // 60
#     seconds %= 60
#     return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
#
#
# robots_data = input().split(';')
# process_time_by_robot = {}
# busy_until_by_robot = {}
#
# for robot_data in robots_data:
#     name, process_time = robot_data.split('-')
#     process_time_by_robot[name] = int(process_time)
#     busy_until_by_robot[name] = -1
#
# time = convert_str_to_seconds(input())
# items = deque()
#
# while True:
#     line = input()
#     if line == 'End':
#         break
#     items.append(line)
#
# while items:
#     time += 1
#     item = items.popleft()
#
#     for name, busy_until in busy_until_by_robot.items():
#         if time >= busy_until:
#             busy_until_by_robot[name] = time + process_time_by_robot[name]
#             print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
#             break
#     else:
#         items.append(item)

# # 08. Crossroads
# from collections import deque
#
# green_window = int(input())
# free_window = int(input())
#
# cars = deque()
# passed_cars = 0
# has_crashed = False
#
# while True:
#     line = input()
#     if line == "END":
#         break
#
#     if line == "green":
#         current_green = green_window
#         while cars and current_green > 0:
#             car = cars.popleft()
#             if current_green >= len(car) or current_green + free_window >= len(car):
#                 passed_cars += 1
#                 current_green -= len(car)
#             else:
#                 print('A crash happened!')
#                 print(f'{car} was hit at {car[current_green + free_window]}.')
#                 has_crashed = True
#                 break
#     else:
#         cars.append(line)
#
#     if has_crashed:
#         break
#
# if not has_crashed:
#     print('Everyone is safe.')
#     print(f'{passed_cars} total cars passed the crossroads.')

# # 09. Key Revolver
# from collections import deque
#
# bullet_price = int(input())
# barrel = int(input())
# bullets = [int(x) for x in input().split()]
# locks = deque(int(x) for x in input().split())
# intelligence = int(input())
# current_barrel = barrel
#
# while bullets and locks:
#     bullet = bullets.pop()
#     if locks[0] >= bullet:
#         locks.popleft()
#         print('Bang!')
#     else:
#         print('Ping!')
#     intelligence -= bullet_price
#     current_barrel -= 1
#     if current_barrel == 0 and bullets:
#         current_barrel = barrel
#         print('Reloading!')
#
# if locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     print(f'{len(bullets)} bullets left. Earned ${intelligence}')

# # 10. Cups and Bottles
# from collections import deque
#
# cups = deque(int(x) for x in input().split())
# bottles = [int(x) for x in input().split()]
# wasted_water = 0
#
# while cups and bottles:
#     bottle = bottles.pop()
#     if bottle < cups[0]:
#         cups[0] -= bottle
#     elif bottle == cups[0]:
#         cups.popleft()
#     else:
#         wasted_water += (bottle - cups.popleft())
# if bottles:
#     print(f"Bottles: {' '.join(str(x) for x in bottles)}")
# if cups:
#     print(f"Cups: {' '.join(str(x) for x in cups)}")
# print(f'Wasted litters of water: {wasted_water}')