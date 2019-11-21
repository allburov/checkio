#!/usr/bin/env checkio --domain=py run bats-bunker

# https://py.checkio.org/mission/bats-bunker/

# While searching for an adventure on the island, our robotic trio found a creepy old bunker.     In the bunker, someone has hidden a rare and powerful computer chip which the robots hope to install on their spaceship.    Our adventurous heroes have tried to search for this chip, but the bunker is occupied by robo-bats and the Alpha Bat appears to be in possession of the chip.    In order to obtain the chip, the robots must capture Alpha Bat.     This is no easy feat though; the bunker is filled with bat scouts which will alert the others if they spot intruders.    If we want to catch the Alpha Bat, we will need to know the amount of time it takes for the alert sent by the scout near the entrance to reach the Alpha Bat.
# 
# We have the advantage that the bunker's walls do not reflect sound, so the alert signals can extend only in a straight line.    The time it takes an alert to move between two bats is proportional to the Euclidean distance between cell centers (see the illustration).    The time for the alert to travel between neighbouring cells is1 second.    Alert "lines" cannot pass through walls or around corners.
# 
# You are given the map of bunker as a list of strings:
# "-" is an empty cell
# "W" is a wall
# "B" is a bat
# "A" is the Alpha Bat
# The entrance is placed at top left cell and there's always a bat right there (be careful, the Alpha bat can be here too).
# 
# You should calculate the minimal possible time for the alert to reach the leader with a precision of two digits (±0.01).
# 
# 
# 
# Input:A map of the bunker as a list of strings.
# 
# Output:The minimal possible time with a precision of two digits as a float.
# 
# Precondition:
# 3 ≤ len(bunker) ≤ 7
# all(3 ≤ len(row) ≤ 7 and len(row) == len(bunker[0]) for row in bunker)
# bunker[0][0] == "B" or bunker[0][0] == "A"
# The Alpha bat can be only one.
# Path from left corner to Alpha Bet always exists.
# 
# 
# END_DESC

def checkio(bunker):
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
