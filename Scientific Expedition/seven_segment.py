#!/usr/bin/env checkio --domain=py run seven-segment

# https://py.checkio.org/mission/seven-segment/

import itertools


# You have a device that uses aSeven-segment displayto display 2 digit numbers.However, some of the segments aren't working and can't be displayed.
#
# You will be given information on the lit and broken segments.You won't know whether the broken segment is lit or not.You have to count and return the total number that the device may be displaying.
#
# The input is a set of lit segments (the first argument) and broken segments (the second argument).
#
# Uppercase letters represent the segments of the first out two digit number.Lowercase letters represent the segments of the second out two digit number.topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', middle: 'G(g)'
#
#
#
# Input:Two arguments. The first one contains the lit segments as a set of letters representing segments. The second one contains the broken segments as a set of letters representing segments.
#
# Output:The total number that the device may be displaying.
#
#
#
# Precondition:
# all(re.match('[A-Ga-g]', s) for s in lit | broken)len(lit  &  broken) == 0
#
#
# END_DESC


class Segment(object):
    NUMBER_MAP = {
        1: set('bc'),
        2: set('abged'),
        3: set('abcdg'),
        4: set('fgbc'),
        5: set('afgcd'),
        6: set('afgcde'),
        7: set('abc'),
        8: set('abcdefg'),
        9: set('abcdfg'),
        0: set('abcdef'),
    }

    def __init__(self, lit, broken, filter_=lambda x: x):
        lit = filter(filter_, lit)
        broken = filter(filter_, broken)
        self.lit = set("".join(lit).lower())
        self.broken = set("".join(broken).lower())

    @property
    def digit(self):
        allow = set()
        for broken_lit in self.get_broken_combinations():
            can_lit = self.lit | broken_lit
            allow |= set((number for number, segment in self.NUMBER_MAP.items() if segment == can_lit))
        return allow

    def get_broken_combinations(self):
        for L in range(0, len(self.broken) + 1):
            for subset in itertools.combinations(self.broken, L):
                yield set(subset)


def seven_segment(lit_seg, broken_seg):
    upper = Segment(lit_seg, broken_seg, str.isupper)
    lower = Segment(lit_seg, broken_seg, str.islower)
    result = len(upper.digit) * len(lower.digit)
    return result


if __name__ == '__main__':
    assert Segment({'A', 'B', 'C', 'D', 'E', 'F'}, 'G').digit == {0, 8}
    assert Segment('BC', 'A').digit == {1, 7}
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4  # 0, 8, 80, 88
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
