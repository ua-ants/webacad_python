import math

def calc_pascals_element(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_tri_row(num):
    res = []
    for element in range(num + 1):
        res.append(calc_pascals_element(num, element))
    return res

print(pascals_tri_row(10))