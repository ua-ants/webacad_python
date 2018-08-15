# Написать функцию которая находит факториал числа.

def factorial(a):
    if a <= 0:
        return 0
    else:
        res = 1
        for i in range(1, a+1):
            res *= i
            print(i)
        return res