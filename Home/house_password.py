#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run house-password

# 
# END_DESC

import string


def checkio(data: str) -> bool:
    strong = all([
        len(data) >= 10,  # len
        set(string.ascii_uppercase) & set(data),  # Upper
        set(string.ascii_lowercase) & set(data),  # Lower
        set(string.digits) & set(data)  # Digit
    ])

    # replace this for solution
    return strong


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")