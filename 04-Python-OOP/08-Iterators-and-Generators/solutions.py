# # # Lab

# # 01. Custom Range
# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = self.start - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         if self.current > self.end:
#             raise StopIteration
#         return self.current

# # 02. Reverse Iter
# class reverse_iter:
#     def __init__(self, collection):
#         self.collection = collection
#         self.start_index = len(self.collection) - 1
#         self.end_index = 0
#         self.current_index = self.start_index + 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_index -= 1
#         if self.current_index < self.end_index:
#             raise StopIteration
#         return self.collection[self.current_index]


# # 02. Vowels
# class vowels:
#     def __init__(self, text):
#         self.text = text
#         self.all_vowels = ['a', 'i', 'e', 'u', 'o', 'y']
#         self.vowels = [char for char in self.text if char.lower() in self.all_vowels]
#         self.current_index = -1
#         self.end_index = len(self.vowels) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_index += 1
#         if self.current_index > self.end_index:
#             raise StopIteration
#         return self.vowels[self.current_index]

# # 04. Squares
# def squares(n):
#     num = 1
#     while num <= n:
#         yield num ** 2
#         num += 1

# # 05. Generator Range
# def genrange(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current += 1

# # 06. Reverse string
# def reverse_text(text):
#     start_i, end_i = len(text) - 1, 0
#     while end_i <= start_i:
#         yield text[start_i]
#         start_i -= 1


# # # Exercise

# # 01. Take Skip
# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#         self.iteration = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.iteration == self.count - 1:
#             raise StopIteration
#         self.iteration += 1
#         return self.iteration * self.step

# # 02. Dictionary Iterator
# class dictionary_iter:
#     def __init__(self, data):
#         self.items = list(data.items())
#         self.idx = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx >= len(self.items) - 1:
#             raise StopIteration
#         self.idx += 1
#         return self.items[self.idx]

# # 03. Countdown Iterator
# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count + 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count <= 0:
#             raise StopIteration
#         self.count -= 1
#         return self.count

# # 04. Sequence Repeat
# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.idx = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx == self.number - 1:
#             raise StopIteration
#         self.idx += 1
#         return self.sequence[self.idx % len(self.sequence)]

# # 05. Take Halves
# def solution():
#     def integers():
#         num = 1
#         while True:
#             yield num
#             num += 1
#
#     def halves():
#         for i in integers():
#             yield i / 2
#
#     def take(n, seq):
#         return [next(seq) for _ in range(n)]
#
#     return take, halves, integers

# # 06. Fibonacci Generator
# def fibonacci():
#     n1, n2 = 0, 1
#     while True:
#         yield n1
#         n1, n2 = n2, n1 + n2

# # 07. Reader
# def read_next(*args):
#     for seq in args:
#         yield from seq

# # 08. Prime Numbers
# from math import sqrt
#
#
# def get_primes(numbers: list):
#     for number in numbers:
#         if number <= 1:
#             continue
#         for divisor in range(2, int(sqrt(number)) + 1):
#             if number % divisor == 0:
#                 break
#         else:
#             yield number

# # 09. Possible permutations
# from itertools import permutations
#
#
# def possible_permutations(sequence):
#     for el in permutations(sequence):
#         yield list(el)
