"""
intersection
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
intersection([2,4,6], [4,2]) # -> [2,4]
"""


def intersection(a, b):
    a1 = set(a) # O(n):space
    res = [] # O(n):space
    # for e in a: #O(n):time
    #   a1.add(e)
    for c in b: #O(m):time
        if c in a1: #constant
            res.append(c)
    return res

# O(n+m)
# time: O(min(n+m))