#!/usr/bin/env checkio --domain=py run domino-chain

# https://py.checkio.org/mission/domino-chain/

# You have a Domino box. Domino tiles contain two numbers from 0 (empty) to 6. Tiles are unordered and 1-6 is the same as 6-1. The double-six set contains 28 unique tiles - all combinations of number pairs.
# 
# Several tiles fell out of the box. You should try to line up a chain from these tiles, compiling them to each other's suitable sides (sides with the same numbers). Thus, you can get a continuous chain of tiles. In some cases, such a chain will not be the only one.
# 
# For example, you've ended up these tiles:
# 1-5, 2-5, 3-5, 4-5, 3-4
# So, with them you can build two complete chains:
# 1-5, 5-3, 3-4, 4-5, 5-2
# 1-5, 5-4, 4-3, 3-5, 5-2
# 
# 
# Your goal in this missionis to count how many complete chains you can make using all of the given dominoes.
# 
# Note.Chains must be unique. An inverted chain is not considered as unique: "1-2, 2-3, 3-4, 4-5" and "5-4, 4-3, 3-2, 2-1" are the same chain.
# 
# Input:String with the description of the domino tiles. Like this one: "5-4, 4-3, 3-2, 2-1".
# 
# Output:Integer. The maximum number of complete chains that you can build using all of the given tiles.
# 
# Precondition:5<= len(given_tiles)<= 17
# 
# 
# END_DESC

def domino_chain(tiles: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")