# Написать аналог функции len

def my_len(a):
    res = 0
    if isinstance(a, str):
        a = list(a)
    if isinstance(a, list):
        res = 0
        while a:
            a.pop()
            res += 1
    else:
        raise ValueError
    return res

