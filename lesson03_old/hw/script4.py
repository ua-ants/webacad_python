import random as r

# generate array:
arr = []
n = r.randint(2, 20)
while (n):
    arr.append(r.randint(0, 21))
    n -= 1
print(arr)


# task 4. реализовать функцию, которая принимает массив, и два параметра,
# где первый параметр - слайс ОТ и второй слайс ДО, по умолчанию первый параметр равен нулю

def slice_array(sfrom=0, **kargs):
    return kargs['sarr'][sfrom:kargs['sto']]


print(slice_array(sto=8, sarr=arr))
print(slice_array(sfrom=2, sto=10, sarr=arr))
