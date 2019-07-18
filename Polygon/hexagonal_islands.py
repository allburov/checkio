#!/usr/bin/env checkio --domain=py run hexagonal-islands

# https://py.checkio.org/mission/hexagonal-islands/

# This is anotherCalculate Islandsusing a hexagonal grid.Please help the robots again.
# 
# The size of the hexagonal grid is 12x9. ('A1' to 'L9'),Alphabets represent columns, numbers represent rows.flat topped.shoves even columns down.You are given a set of coastal hexes for all islands as input value.You have to find all islands that they represent and return an list of that size. (list, tuple or iterable)
# 
# Note:The islands doesn't include  other islands.
# 
# 
# END_DESC

from typing import Set, Iterable


def hexagonal_islands(coasts: Set[str]) -> Iterable[int]:

    return []


if __name__ == '__main__':
    assert(sorted(hexagonal_islands({'C5', 'E5', 'F4', 'F5', 'H4', 'H5', 'I4', 'I6', 'J4', 'J5'}))) == [1, 3, 7]
    assert(sorted(hexagonal_islands({'A1', 'A2', 'A3', 'A4', 'B1', 'B4', 'C2', 'C5', 'D2', 'D3', 'D4', 'D5',
                                     'H6', 'H7', 'H8', 'I6', 'I9', 'J5', 'J9', 'K6', 'K9', 'L6', 'L7', 'L8'}))) == [16, 19]
    print('The local tests are done. Click on "Check" for more real tests.')