#!/usr/bin/env checkio --domain=py run roman-numerals
# END_DESC
import collections

LEVEL_ROMAN = {
    0: ('I', 'V', 'X'),
    1: ('X', 'L', 'C'),
    2: ('C', 'D', 'M'),
    3: 'M' * 3
}


def to_roman_sym(v: str, level: int):
    """Convert one value beetwen 1 to 10 to roman, depending on the level"""
    v = int(v)
    l1, l5, l10 = LEVEL_ROMAN[level]
    result = {
        1: l1,
        2: l1 * 2,
        3: l1 * 3,
        4: l1 + l5,
        5: l5,
        6: l5 + l1,
        7: l5 + l1 + l1,
        8: l5 + l1 + l1 + l1,
        9: l1 + l10,
        10: l10,
    }
    repr = result.get(v, '')
    return repr


def first_solution(data: int) -> str:
    result = []
    for level, s in enumerate(reversed(str(data))):
        result.append(to_roman_sym(s, level))
    repr = ''.join(reversed(result))
    return repr


def bisect_solution(data: int) -> str:
    roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # TODO:


checkio = first_solution

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio(3) == 'III', '3'
    assert checkio(4) == 'IV', '4'
    assert checkio(5) == 'V', '5'
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio(76) == 'LXXVI'
    assert checkio(13) == 'XIII'
    assert checkio(44) == 'XLIV'
    assert checkio(3999) == 'MMMCMXCIX'
    print('Done! Go Check!')
