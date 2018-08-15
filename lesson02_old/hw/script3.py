# given array:
arr = [1, 3, 'a', 5, 5, 3, 'a', 5, 3, 'str01', 6, 3, 'str01', 1]

# task 3. Удалить в массиве первый и последний элементы.

def remove_last_and_first(arr):
    del arr[0]
    del arr[-1]
    return arr

print("Array before: ", arr)
print("Array after: ", remove_last_and_first(arr))