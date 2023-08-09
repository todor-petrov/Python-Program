# # # Lab

# # 01. 01. Custom Range
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
#         self.iteration = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.iteration == self.count:
#             raise StopIteration
#         result = self.iteration * self.step
#         self.iteration += 1
#         return result

# 02.
