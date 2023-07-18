number, result = float(input()), ''
if 0 < abs(number) < 1:
    result = 'small '
elif 1000000 < abs(number):
    result = 'large '
if number == 0:
    result = 'zero'
elif number > 0:
    result += 'positive'
else:
    result += 'negative'
print(result)
