#!/usr/bin/env checkio --domain=py run colder-warmer

# https://py.checkio.org/mission/colder-warmer/

# Let's play a game of hide and seek. You have been given a map of 10x10 cells and in one of the cells we've hidden your goal.    You can move to and from any cell in the field.    On each move you'll get informed if the move places you closer or further away from your goal, compared to your previous location.    Your function compiles data about previous steps, each step is a list of list, where first and second elements are    your coordinates (row and column) and third is the info on how much closer you've gotten (colder or warmer) -- "colder" is -1, "warmer" is 1 and "same" is 0.    For your measurement of the distance to the goal you should use the Euclidean distance. At each step you need to return the coordinates for your next step.    If your step places you within the goal cell, then you win! You should find the goal within12steps.
# 
# 
# 
# Input:Information about previous steps as a list of lists.    Each list contains coordinates and status alteration (warm, cold same).
# 
# Output:The coordinates of your new move as a list/tuple of two integers.
# 
# Precondition:|map| = 10x10
# 
# 
# 
# END_DESC

def checkio(steps):

    return [0, 0]

if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    from math import hypot
    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"