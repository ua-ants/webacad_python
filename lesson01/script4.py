# Программа запрашивает у пользователя строку и выводит ее по центру в таблице 20х3.

line = input('Enter a string: ')

print('x'*20)
print('x{:^18s}x'.format(line))
print('x'*20)