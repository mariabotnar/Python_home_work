import math

def square (a):
    s = a ** 2
    return s

a = float(input('Cторона квадрата: '))
result = square(a)
rounded_result = math.ceil(result)
print(f'Округлённая в большую сторону площадь квадрата - {rounded_result}')
