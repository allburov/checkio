#!/usr/bin/env checkio --domain=py run ground-for-the-house

# https://py.checkio.org/mission/ground-for-the-house/

# 
# END_DESC

TOO_MUCH = 100


def house(plan):
    lines = [x for x in plan.splitlines() if x]

    up = TOO_MUCH
    down = 0
    left = TOO_MUCH
    right = 0
    for i, line in enumerate(lines, start=1):
        lpos = line.find('#') + 1
        rpos = line.rfind('#') + 1
        # No # in line
        if lpos == 0:
            continue
        up = min(i, up)
        down = max(down, i)
        left = min(lpos, left)
        right = max(rpos, right)

    if up == TOO_MUCH:
        return 0

    for var in ('up', 'down', 'left', 'right'):
        print(var, '=', locals()[var])

    house_square = (down - up + 1) * (right - left + 1)
    print(f'Square = {house_square}')
    return house_square

