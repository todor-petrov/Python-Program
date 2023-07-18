# 01. Number Definer
number, result = float(input()), ''
if number == 0:
    result = 'zero'
elif 0 < number:
    result = 'positive'
else:
    result = 'negative'
if 0 < abs(number) < 1:
    result = 'small ' + result
if 1000000 < abs(number):
    result = 'large ' + result
print(result)