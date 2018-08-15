while True:
    print('To quit program enter "q"')
    val1 = input('Enter a first number: ')

    if val1 == 'q':
        break

    val2 = input('Enter a second number: ')

    if val2 == 'q':
        break

    try:
        val1 = int(val1)
        val2 = int(val2)
    except ValueError:
        print('one of entered value is not integer')
        continue

    if val1 > val2:
        print(val1-val2)
    elif val1 < val2:
        print(val1+val2)
    else:
        print(val1)
