# # # Lab


# # 01. Multiplication Functon
# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)

# # 02. Person Info
# def get_info(**kwargs):
#     name = kwargs['name']
#     town = kwargs['town']
#     age = kwargs['age']
#     return f'This is {name} from {town} and he is {age} years old'

# # 03. Cheese Showcase
# def sorting_cheeses(**kwargs):
#     data = kwargs
#     for k, v in data.items():
#         data[k] = sorted(v)[::-1]
#     final = {k: v for k, v in sorted(data.items(), key=lambda x: (-len(x[1]), x[0]))}
#     result = []
#     for k, v in final.items():
#         result.append(k)
#         result.extend([str(x) for x in v])
#     return '\n'.join(result)

# # 04. Rectangle
# def rectangle(length, width):
#
#     if not isinstance(length, int) or not isinstance(width, int):
#         return 'Enter valid values!'
#
#     def area():
#         return length * width
#
#     def perimeter():
#         return (length + width) * 2
#
#     return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'

# # 05. Recursive Power
# def recursive_power(number, power):
#     if power == 0:
#         return 1
#     return number * recursive_power(number, power - 1)

# # 06. Operate
# from functools import reduce
#
#
# def operate(operator, *args):
#     if operator == '+':
#         return reduce(lambda x, y: x + y, args)
#     if operator == '-':
#         return reduce(lambda x, y: x - y, args)
#     if operator == '*':
#         return reduce(lambda x, y: x * y, args)
#     if operator == '/':
#         return reduce(lambda x, y: x / y, args)


# # # Exercise

# # 01. Negative vs Positive
# def negative_sum(nums):
#     return sum([x for x in nums if x < 0])
#
#
# def positive_sum(nums):
#     return sum([x for x in nums if x > 0])
#
#
# def difference(nums):
#     if abs(positive_sum(nums)) > abs(negative_sum(nums)):
#         return 'The positives are stronger than the negatives'
#     return 'The negatives are stronger than the positives'
#
#
# numbers = [int(x) for x in input().split(' ')]
# print(negative_sum(numbers))
# print(positive_sum(numbers))
# print(difference(numbers))

# # 02. Keyword Arguments Length
# def kwargs_length(**kwargs):
#     return len(kwargs)


# # 03. Even or Odd
# def even_odd(*args):
#     result = {'even': [x for x in args[:-1] if x % 2 == 0],
#               'odd': [x for x in args[:-1] if x % 2 != 0]}
#     return result[args[-1]]

# # 04. Numbers Filter
# def even_odd_filter(**kwargs):
#     data = {}
#     for k in kwargs:
#         if k == 'even':
#             data[k] = [x for x in kwargs[k] if x % 2 == 0]
#         else:
#             data[k] = [x for x in kwargs[k] if x % 2 != 0]
#     sorted_data = {k: v for k, v in sorted(data.items(), key=lambda x: -len(x[1]))}
#     return sorted_data

# # 05. Concatenate
# def concatenate(*args, **kwargs):
#     line = ''.join(args)
#     for k, v in kwargs.items():
#         line = line.replace(k, v)
#     return line

# 06. Function Executor
# def func_executor(*args):
#     result = []
#     for tuple_ in args:
#         result.append(f'{tuple_[0].__name__} - {tuple_[0](*tuple_[1])}')
#     return '\n'.join(result)

# # 07. Grocery
# def grocery_store(**kwargs):
#     result = []
#     sorted_receipt = {k: v for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))}
#     for p, q in sorted_receipt.items():
#         result.append(f'{p}: {q}')
#     return '\n'.join(result)

# # 08. Age Assignment
# def age_assignment(*args, **kwargs):
#     result = []
#     for name in sorted(args):
#         result.append(f'{name} is {kwargs[name[0]]} years old.')
#     return '\n'.join(result)

# # 09. Recursion Palindrome
# def palindrome(text, idx):
#     if idx == len(text) // 2:
#         return f'{text} is a palindrome'
#
#     left = text[idx]
#     right = text[len(text) - 1 - idx]
#
#     if left != right:
#         return f'{text} is not a palindrome'
#
#     return palindrome(text, idx + 1)

# # 10. Fill the Box
# from collections import deque
#
#
# def fill_the_box(height, length, width, *args):
#     volume = height * length * width
#     i = args.index('Finish')
#     cubes = deque(args[:i])
#     while cubes:
#         if cubes[0] <= volume:
#             volume -= cubes.pop()
#         else:
#             cubes[0] -= volume
#             volume = 0
#             break
#     if volume == 0:
#         return f"No more free space! You have {sum(cubes)} more cubes."
#     return f"There is free space in the box. You could put {volume} more cubes."

# # 11. Math Operations
# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     numbers = deque([float(x) for x in args])
#     operations, count = kwargs, 0
#     while numbers:
#         number = numbers.popleft()
#         count += 1
#         if count == 5:
#             count = 1
#         if count == 1:
#             operations['a'] += number
#         elif count == 2:
#             operations['s'] -= number
#         elif count == 3 and number != 0:
#             operations['d'] /= number
#         elif count == 4:
#             operations['m'] *= number
#
#     sorted_dict = {k: v for k, v in sorted(operations.items(), key=lambda x: (-x[1], x[0]))}
#     result = []
#     for k, v in sorted_dict.items():
#         result.append(f'{k}: {v:.1f}')
#
#     return '\n'.join(result)