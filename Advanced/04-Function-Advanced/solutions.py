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
