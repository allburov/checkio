#!/usr/bin/env checkio --domain=py run yaml-more-types

# https://py.checkio.org/mission/yaml-more-types/

# This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The data types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in strings.
# 
# Here are some of the examples:
# 
# 
# name: "Bob Dylan"
# children: 6
# 
# {
#   "name": "Bob Dylan", 
#   "children": 6
# }
# As you can see, the string can be put in quotes. It can be both double and single quotes.
# 
# 
# name: "Bob Dylan"
# children: 6
# alive: false
# 
# {
#   "name": "Bob Dylan", 
#   "alive": False, 
#   "children": 6
# }
# true and false are the keywords defining the boolean type.
# 
# 
# name: "Bob Dylan"
# children: 6
# coding:
# 
# {
#   "coding": None, 
#   "name": "Bob Dylan", 
#   "children": 6
# }
# If no value is specified, it becomes undefined. There also is a keyword for this - null.
# 
# Input:A format string.
# 
# Output:An object.
# 
# Precondition:YAML 1.2 is being used withJSON Schema.
# 
# 
# END_DESC

def yaml(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")