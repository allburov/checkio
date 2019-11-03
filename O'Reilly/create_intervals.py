#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run create-intervals

# From a set of ints you have to create a list of closed intervals as tuples, so the  intervals are covering all the values found in the set.
# 
# A closed interval includes its endpoints! The interval1..5, for example,  includes each valuexthat satifies the condition1<= x<= 5.
# 
# Values can only be in the same interval if the difference between a value and the next  smaller value in the set equals one, otherwise a new interval begins. Of course, the  start value of an interval is excluded from this rule.
# A single value, that does not fit into an existing interval becomes the start- and  endpoint of a new interval.
# 
# Input:A set of ints.
# 
# Output:A list of tuples of two ints, indicating the endpoints of the interval. The Array should be sorted by start point of each interval
# 
# 
# END_DESC

def create_intervals(data):
    if not data:
        return []
    result = []
    data = sorted(data)
    start = data[0]
    for i in range(1, len(data)):
        if data[i] != data[i - 1] + 1:
            result.append((start, data[i - 1]))
            start = data[i]

    result.append((start, data[-1]))
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals([]) == []
    assert create_intervals([1]) == [(1, 1)]
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12, 14}) == [(1, 5), (7, 8), (12, 12), (14, 14)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals({1, 3, 5, 7}) == [(1, 1), (3, 3), (5, 5), (7, 7)], "Second"
    print('Almost done! The only thing left to do is to Check it!')