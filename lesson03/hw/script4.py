# Вывести на экран 10 первых простых чисел используя функцию задания 1

def is_prime(a):
    for i in range(2, abs(a)):
        if a % i == 0:
            return False
    return True

count = 10
num = 1
while(count):
    if is_prime(num):
        print(num)
        count -= 1
    num += 1