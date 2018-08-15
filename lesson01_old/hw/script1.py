while True:
    print('To quit program enter "q"')
    a = input('Enter a number: ')

    if a == 'q':
        break

    try:
        a = int(a)
    except ValueError:
        print('value is not integer')
        continue

    for i in range(2, a):
        if a%i == 0:
            print('number is not prime')
            a = 4
            break

    if a != 4:
        print('number is prime')