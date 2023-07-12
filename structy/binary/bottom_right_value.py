"""
bottom right value
Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty.
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_right_value(root):
    height, value = 0, 0
    stack = [(root, 0)]
    while stack:
        node, count = stack.pop()
        if not node.right and count >= height:
            height, value = count, node.val
        if node.right:
            stack.append((node.right, count + 1))
        if node.left:
            stack.append((node.left, count + 1))
    return value


# def bottom_right_value(root):
#   queue = deque([root])
#   res = None
#   while queue:
#     node = queue.popleft()
#     res = node.val
#     if node.left:
#       queue.append(node.left)
#     if node.right:
#       queue.append(node.right)
#   return res


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \
#    -2  6


print(bottom_right_value(a))  # -> 6
