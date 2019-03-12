#!/usr/bin/env checkio --domain=py run the-ship-teams

# https://py.checkio.org/mission/the-ship-teams/

# 
# END_DESC


def two_teams(sailors):
    crew = lambda fn: sorted(x for x, y in filter(fn, sailors.items()))
    middle = crew(lambda x: 20 <= x[1] <= 40)
    older = crew(lambda x: x[1] > 40 or x[1] < 20)
    return [older, middle]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
               ['Abrahams', 'Coleman'],
               ['Smith', 'Wesson']
           ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
               ['Fernandes', 'Kale', 'McCortney'],
               ['Johnson']
           ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
