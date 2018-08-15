#given string
str1 = 'some string'

# task 3. реализовать функцию, которая которая принимает строку,
# и возвращает эту строку в обратном порядке

def reverse_stirng(str):
    i = 1
    res = ''
    while(i <= str.__len__()):
        res += str[str.__len__() - i]
        i += 1
    return res

print(reverse_stirng(str1))