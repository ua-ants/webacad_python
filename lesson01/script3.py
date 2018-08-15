# Программа должна переводить число, введенное с клавиатуры в метрах, в километры.

distance = input('Enter distance in meters: ')

try:
    distance = int(distance)
except ValueError:
    print('Distance should be integer')
else:
    print('Distance in km is: {km}'.format(km = distance / 1000))