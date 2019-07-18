#!/usr/bin/env checkio --domain=py run delivery-drone

# https://py.checkio.org/mission/delivery-drone/

# Today drones working in transportation. (Delivery drone(Wikipedia))Let's plan efficient drone movement.
# 
# The input value is a list of integers.One or more number of this represent the existence of the package to be transported and its destinationYou have to return the shortest moving distance for the drone to complete all transportation as an integer.
# 
# Note:The drone is initially at position 0 (most left).The drone can carry only one package at a time.You can only drop a package on destination.The drone finallyreturnsto position 0.
# END_DESC

from typing import List


def delivery_drone(orders: List[int]) -> int:

    return 0


if __name__ == '__main__':
    assert delivery_drone([0, 2, 0]) == 4
    assert delivery_drone([0, 0, 1, 2]) == 6
    assert delivery_drone([0, 2, 4, 0, 1, 0, 5]) == 12
    print('The local tests are done. Click on "Check" for more real tests.')