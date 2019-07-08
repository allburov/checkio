#!/usr/bin/env checkio --domain=py run binary-count

# https://py.checkio.org/mission/binary-count/

# 
# END_DESC
from math import sqrt


def checkio(number: int) -> int:
    number1 = 0
    # находим степень двойки, больше этого числа
    max_exp = int(sqrt(number)) + 1

    # По всем степеням дойки от MAX до 0 делаем, если число меньше.
    for i in range(max_exp - 1, -1, -1):
        if 2 ** i <= number:
            number -= 2 ** i
            number1 += 1
        if number == 0:
            return number1
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2**32)
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
