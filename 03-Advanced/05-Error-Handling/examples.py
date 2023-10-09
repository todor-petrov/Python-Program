# # 01. So Many Exceptions
#
# numbers_list = [int(x) for x in input().split(', ')]
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(result)


# # 02. Value Cannot Be Negative
# class ValueCannotBeNegative(Exception):
#     pass
#
#
# cycles = 5
# for i in range(cycles):
#     number = int(input())
#     if number < 0:
#         raise ValueCannotBeNegative
