#!/usr/bin/env checkio --domain=py run power-supply

# https://py.checkio.org/mission/power-supply/

# You are given the power grid and power-plant's information    (plant-number and supply-range). You should find out which cities blacked out.    A power plant can supply itself and connected cities with power, but the range is    limited.
# 
# 
# 
# Input:Two arguments. The first one is the network, represented as a list of connections.    Each connection is a list of two nodes that are connected. A city or power plant can    be a node. Each city or power plant is a unique string. The second argument is a dict    where keys are power plants and values are the power plant's range.
# 
# Output:A set of strings.         Each string is the name of a blacked out city.
# 
# Precondition:len(set(chain(*networks)))<= 25
# 
# 
# END_DESC
from collections import defaultdict


def power_supply(network, power_plants):
    network_graph = defaultdict(set)
    # Parse
    for f1, f2 in network:
        network_graph[f1].add(f2)
        network_graph[f2].add(f1)

    visited = {x: False for x in network_graph.keys()}

    def bfs(start, level):
        visited[start] = True
        if level == 0:
            return
        for neighbor in network_graph[start]:
            bfs(neighbor, level - 1)

    for plant, power in power_plants.items():
        bfs(plant, power)

    not_visited = set(x for x, visit in visited.items() if not visit)
    return not_visited
