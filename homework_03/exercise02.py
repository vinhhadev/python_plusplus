import math

x = float(input('Nhập số x = '))
y = float(input('Nhập số y = '))
z = float(input('Nhập số z = '))

F = (x + y + z) / (math.pow(x, 2) + math.pow(y, 2) + 1) - abs(x - z * math.cos(y))

print(f'Giá trị của F là: {F}')