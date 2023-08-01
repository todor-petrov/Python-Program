class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        result = '['
        final_line = sorted(self.data)[::-1]
        for i in range(len(final_line)):
            if i == len(final_line) - 1:
                result += final_line[i] + ']'
            else:
                result += final_line[i] + ', '
        return f"{result}"


line = Stack()
line.push('apple')
line.push('carrot')
line.push('banana')
print(line)