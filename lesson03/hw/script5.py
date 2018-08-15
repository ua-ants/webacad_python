# Написать функцию, которая выводит на экран n первых четных чисел.

def print_even(n):
    num = 1
    while n:
        if num % 2 == 0:
            print(num)
            n -= 1
        num += 1
