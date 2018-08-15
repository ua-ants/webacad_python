import random as r

# generate array:
arr=[]
n = r.randint(2, 20)
while(n):
    arr.append(r.randint(0, 21))
    n -= 1
print(arr)

# task 9. Дан список целых чисел. Посчитать сумму всех чисел массива,
# при учете, что числа в промежутке от 13 до 19 включительно,
# должны приравниваться нулю, за исключением 15 и 16.


def count_all_except(arr):
    res = 0
    for i in arr:
        if i in range(13, 20) and i not in [15, 16]:
            continue
        res += i
    return res

print(count_all_except(arr))