#!/usr/bin/env checkio --domain=py run speechmodule

# https://py.checkio.org/mission/speechmodule/

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
# 
# Input:A number as an integer.
# 
# Output:The string representation of the number as a string.
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

FIRST_TEN = [None, "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
OTHER_TENS = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

to_map = lambda x: {i: x[i - 1] for i in range(0, 11)}

FIRST_TEN = to_map(FIRST_TEN)
OTHER_TENS = to_map(OTHER_TENS)


def checkio(number):
    answer = []

    # e.g. 123
    hundred = number // 100  # 1
    ten11 = number % 100  # 23
    ten10 = ten11 // 10  # 2
    ten = number % 10  # 3

    answer += FIRST_TEN[hundred] * bool(hundred)
    answer += HUNDRED * bool(hundred)

    if ten11 in SECOND_TEN:
        answer += SECOND_TEN[ten11] * (ten11 in SECOND_TEN)
    else:
        answer += OTHER_TENS[ten10]
        answer += [FIRST_TEN[ten]] * bool(ten)
    return " ".join(answer)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
