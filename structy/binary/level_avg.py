"""
 averages
    Write a function, level_averages, that takes in the root of a binary tree that
 contains number values.
 The function should return a list containing the average value of each level.
"""

from statistics import mean


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_averages(root):
    levels = []
    _level_averages(root, levels, 0)
    return [mean(level) for level in levels]  # return mean of every level, sub array paths


def _level_averages(root, levels, level_num):
    if not root:
        return []

    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    _level_averages(root.left, levels, level_num + 1)
    _level_averages(root.right, levels, level_num + 1)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(level_averages(a))  # -> [ 3, 7.5, 1 ]
