#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run find-friends

# Sophia's drones are not soulless and stupid drones; they can make and have friends.    In fact, they already are working for the their own social network just for drones!    Sophia has received the data about the connections between drones and she wants to know more about relations between them.
# 
# We have an array of straight connections between drones.    Each connection is represented as a string with two names of friends separated by hyphen.    For example: "dr101-mr99" means what thedr101andmr99are friends.    Your should write a function that allow determine more complex connection between drones.    You are given two names also. Try to determine if they are related through common bonds by any depth.    For example: if two drones have a common friends or friends who have common friends and so on.
# 
# 
# 
# Let's look at examples:
# scout2andscout3have the common friendscout1so they are related.superandscout2are related throughsscout,scout4andscout1.    Butdr101andsscoutare not related.
# 
# Input:Three arguments: Information about friends as a tuple of strings; first name as a string;    second name as a string.
# 
# Output:Are these drones related or not as a boolean.
# 
# Precondition:len(network) ≤ 45
# if"name1-name2"innetwork, then"name2-name1"not innetwork
# 3 ≤ len(drone_name) ≤ 6
# first_nameandsecond_nameinnetwork.
# 
# 
# END_DESC

from collections import defaultdict


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def check_connection(network, first, second):
    network_graph = defaultdict(set)
    # Parse
    for friendship in network:
        f1, f2 = friendship.split('-')
        network_graph[f1].add(f2)
        network_graph[f2].add(f1)
    # find path https://www.python.org/doc/essays/graphs/
    sp = find_shortest_path(network_graph, first, second)
    return bool(sp)