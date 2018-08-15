# Вычислить возраст человека. Программа принимает с клавиатуры год рождения и выводит возраст на экран.

import datetime as d

birth_year = input('Enter year of birth: ')

try:
    birth_year = int(birth_year)
except ValueError:
    print('Year should be integer')
else:
    if birth_year > d.datetime.now().year or birth_year < 0:
        print('invalid year')
    elif birth_year >= d.datetime.now().year - 1:
        print('You are: {age} year old'.format(age = d.datetime.now().year - birth_year))
    else:
        print('You are: {age} years old'.format(age=d.datetime.now().year - birth_year))
