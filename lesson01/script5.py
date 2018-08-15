# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы
# в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

MINS_IN_HOUR = 60
MINS_IN_DAY = 24 * MINS_IN_HOUR

mins = input('Enter minutes: ')

try:
    mins = int(mins)
except ValueError:
    print('Number of minutes should be integer')
else:
    while abs(mins) >= MINS_IN_DAY:
        if mins < 0:
            mins += MINS_IN_DAY
        else:
            mins -= MINS_IN_DAY

    if mins < 0:
        if mins % MINS_IN_HOUR != 0:
            h = 24 + int(mins / MINS_IN_HOUR) - 1
            m = mins % MINS_IN_HOUR
        else:
            h = 24 + int(mins / MINS_IN_HOUR)
            m = 0
    else:
        h = int(mins / MINS_IN_HOUR)
        m = mins % MINS_IN_HOUR

    print('{h:02d}:{m:02d}'.format(h = h, m = m))