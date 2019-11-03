#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run days-diff

# How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We could make    this a real challenge though and count the difference between any dates.
# 
# You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be    (1982, 4, 19). You should find the difference in days between the given dates. For example between today and    tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute    value.
# 
# Input:Two dates as tuples of integers.
# 
# Output:The difference between the dates in days as an integer.
# 
# Precondition:Dates between 1 january 1 and 31 december 9999.    Dates are correct.
# 
# 
# END_DESC

from datetime import date


def days_diff(a, b):
    return abs((date(*a) - date(*b)).days)