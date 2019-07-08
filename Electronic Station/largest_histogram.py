#!/usr/bin/env checkio --domain=py run largest-histogram

# https://py.checkio.org/mission/largest-histogram/

# "Your power to choose can never be taken from you.
# It can be neglected and it can be ignored.
# But if used, it can make all the difference."
# ― Steve Goodier
# 
# You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.
# 
# Input:List of all rectangles heights in histogram
# 
# Output:Area of the biggest rectangle
# 
# Example:
# 
# 
# largest_histogram([5]) == 5
# largest_histogram([5, 3]) == 6
# largest_histogram([1, 1, 4, 1]) == 4
# largest_histogram([1, 1, 3, 1]) == 4
# largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
# How it is used:There is no way the solution you come up with will be any useful in a real life. Just have some fun here.
# 
# Precondition:
# 0 < len(data) < 1000
# 
# 
#
# END_DESC


# split list like str.split() (from boltons: https://github.com/mahmoud/boltons/blob/master/boltons/iterutils.py)
def split(src, sep):
    return list(x for x in split_iter(src, sep, None) if x)


def split_iter(src, sep=None, maxsplit=None):
    """
    :param src:
    :param sep:
    :param maxsplit:
    :return:
    """
    if maxsplit is not None:
        maxsplit = int(maxsplit)
        if maxsplit == 0:
            yield [src]
            return

    sep_func = lambda x: x == sep

    cur_group = []
    split_count = 0
    for s in src:
        if maxsplit is not None and split_count >= maxsplit:
            sep_func = lambda x: False
        if sep_func(s):
            if sep is None and not cur_group:
                # If sep is none, str.split() "groups" separators
                # check the str.split() docs for more info
                continue
            split_count += 1
            yield cur_group
            cur_group = []
        else:
            cur_group.append(s)

    if cur_group or sep is not None:
        yield cur_group
    return


assert split([1, 1, 0, 0, 1], sep=0) == [[1, 1], [1]]


def largest_histogram(histogram):
    bigger = 0
    # We remove one level and count how much
    for level in range(1, max(histogram) + 1):
        # count how much lenght
        non_null_len = list(map(len, split(histogram, 0))) or [0]
        bigger = max(bigger, max(non_null_len) * level)
        # remove one level
        histogram = [x - 1 if x > 0 else 0 for x in histogram]

    return bigger


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
