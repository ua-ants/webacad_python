while True:
    print('To quit program enter "q"')
    day = input('Enter a day: ')

    if day == 'q':
        break

    try:
        day = int(day)
    except ValueError:
        print('value is not integer')
        continue

    if day < 1 or day > 31:
        print('invalid day')
        continue

    if day < 10:
        print('day in first decade of the month')
    elif day < 20:
        print('day in second decade of the month')
    else:
        print('day in third decade of the month')