import random as r

# generate array:
arr=[]
n = r.randint(2, 20)
while(n):
    arr.append(r.randint(0, 21))
    n -= 1
print(arr)

# task 1. написать функцию find, которая принимает число и массив
# и возвращает количество найденых элементов в массиве числа (.count()),
# если они есть или None, если их нет

def find(num, arr):
    if num not in arr:
        return None
    return arr.count(num)

print(find(5, arr))