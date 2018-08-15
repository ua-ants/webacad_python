# given array:
arr = [1, 3, 'a', 5, 5, 3, 'a', 5, 3, 'str01', 6, 3, 'str01', 1]

# task 2. Определите, есть ли в массиве повторяющиеся элементы. (in)

def array_elements_count(arr):
    elements = set(arr)
    result_map = {}
    for e in elements:
        if arr.count(e) > 1:
            result_map[e] = arr.count(e)
    return result_map

print("Repetitive elements in array: ", array_elements_count(arr))