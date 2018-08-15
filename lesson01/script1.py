# Запрограммировать следующее выражение: (a + b - f / a) + f * a * a - (a + b) Числа а, b, f вводятся с клавиатуры.
# Организовать пользовательский интерфейс, таким образом, чтобы было понятно, в каком порядке должны вводиться числа.

a = input('Enter A: ')
b = input('Enter B: ')
f = input('Enter F: ')

try:
    a = int(a)
    b = int(b)
    f = int(f)
except ValueError:
    print('One or more of values is not integer')
else:
    print('Result: ', a + b - f / a + f * a * a - (a + b))