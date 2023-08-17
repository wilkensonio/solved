"""
Write a function, tree_min_value, that takes in the root
of a binary tree that contains number values. The function
 should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value_recur(root):
    if not root:
        return float('inf')
    return min(
        tree_min_value_recur(root.left)
        , tree_min_value_recur(root.right)
        , root.val
    )


def tree_min_value(root, min_num=float('inf')):
    queue = deque([root])
    while queue:
        visited = queue.pop()
        if visited.val < min_num:
            min_num = visited.val
        if visited.left:
            queue.append(visited.left)
        if visited.right:
            queue.append(visited.right)
    return min_num


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
print(tree_min_value(a))  # -2
print(tree_min_value_recur(a))
