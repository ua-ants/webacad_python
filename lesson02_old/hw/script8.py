import random as r

# generate array:
arr=[]
n = r.randint(2, 20)
while(n):
    arr.append(r.randint(100, 999))
    n -= 1
print(arr)

# task 8. Дан список из целых чисел длинной в три числа. Определить какое число
# наибольшее и вернуть новый список такой же длины, состоящий из максимального
# числа исходного списка.

def find_max_in_array(arr):
    max=arr[0]
    for i in arr:
        if max < i:
            max = i
    return max

def create_array_maxs(arr):
    res = []
    n = arr.__len__()
    while(n):
        res.append(find_max_in_array(arr))
        n -= 1
    return res

print(create_array_maxs(arr))