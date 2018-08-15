# given array:
arr = [1, 3, 'a', 5, 5, 3, 'a', 5, 3, 'str01', 6, 3, 'str01', 1]

# task #1. Найдите количество различных элементов данного массива.(in)

def find_element_number(el, arr):
    res = 0
    for e in arr:
        if e == el:
            res += 1
    return res

print("Number of '{el}' elements in array is: {num}".format(el=5, num = find_element_number(5, arr)))
print("Number of '{el}' elements in array is: {num}".format(el='a', num = find_element_number('a', arr)))