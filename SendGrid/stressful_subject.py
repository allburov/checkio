#!/usr/bin/env checkio --domain=py run stressful-subject

# https://py.checkio.org/mission/stressful-subject/

import re

#
# END_DESC
from itertools import groupby


def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if subj.endswith("!!!"):
        return True

    if subj.upper() == subj:
        return True

    # "red" words
    stress = ["help", "asap", "urgent"]
    stress_chars = set("".join(stress))
    words = subj.lower().split()
    for word in words:
        word = re.sub(f'[^{"".join(stress_chars)}]', '', word)
        word = ''.join([k[0] for k in groupby(word)])
        if word in stress:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I neeed HEeeLP") == True, "Second"
    assert is_stressful("We need you AA.S.AA.P.!!") == True, "Second"
    print('Done! Go Check it!')
