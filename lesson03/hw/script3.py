# Написать функцию is_prime(a), Которая принимает число и возвращает True или False в зависимости от того,
# простое это число или нет (см. https://ru.wikipedia.org/wiki/Простое_число)

def is_prime(a):
    for i in range(2, abs(a)):
        if a % i == 0:
            return False
    return True