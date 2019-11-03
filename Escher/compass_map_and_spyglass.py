#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run compass-map-and-spyglass

# 
# END_DESC
from itertools import product


def next_points(sx, sy, maxx=100, maxy=100):
    """
    Generate available moves from x,y
    """
    variants = [-1, 0, 1]
    diffs = set(product(variants, variants)) - {(0, 0)}
    for i in diffs:
        x, y = sx - i[0], sy - i[1]
        if 0 <= x <= maxx and 0 <= y <= maxy:
            yield (x, y)


def navigation(seaside):
    char_dist = dict(C=0, M=0, S=0)

    # Find start
    sx, sy = 0, 0
    for i, line in enumerate(seaside):
        if 'Y' in line:
            pos = line.index('Y')
            sx = i
            sy = pos
            break

    # BFS
    visited = {(sx, sy): True}
    level = []
    i = 0
    maxx = len(seaside) - 1
    maxy = len(seaside[0]) - 1
    level.append([(sx, sy)])
    while level[i]:
        level.append([])
        for node in level[i]:
            for neighbour in next_points(node[0], node[1], maxx, maxy):
                if neighbour not in visited:
                    value = seaside[neighbour[0]][neighbour[1]]
                    if value in char_dist:
                        char_dist[value] = i + 1
                    visited[neighbour] = i
                    level[i + 1].append(neighbour)
        i = i + 1

        # We found all
        if all(char_dist.values()):
            break

    return sum(char_dist.values())

