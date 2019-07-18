#!/usr/bin/env checkio --domain=py run funny-adding

# https://py.checkio.org/mission/funny-adding/

# We have an array of two positive integers. Add these two numbers together.
# 
# Input:A list of two elements. Each element is a positive integer.
# 
# Output:The sum_n of two numbers.
# 
# 
# END_DESC

def checkio(data):
    """The sum_n of two integer elements"""
    a, b = data
    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')