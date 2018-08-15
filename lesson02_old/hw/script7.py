import random as r

# generate array:
arr=[]
n = r.randint(2, 20)
while(n):
    arr.append(r.randint(100, 999))
    n -= 1
print(arr)

# task 7. Дан список из целых чисел длинной в три числа. Вернуть
# список отсортированный в обратном порядке, не используя метод .reverse()

def reverse_array(arr):
    i = 1
    res = []
    while(i <= arr.__len__()):
        res.append(arr[arr.__len__() - i])
        i += 1
    return res

print(reverse_array(arr))