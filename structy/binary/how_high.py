"""
how high
Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def how_high(root):
    if not root:
        return -1
    max_len = 0
    stack = [(root, 0)]
    while stack:
        node, count = stack.pop()

        if not node.left and not node.right and max_len < count:
            max_len = count
        if node.right:
            stack.append((node.right, count + 1))
        if node.left:
            stack.append((node.left, count + 1))
    return max_len


# def how_high(root):
#   if not root:
#     return -1

#   left_height = how_high(root.left)
#   right_height = how_high(root.right)

#   # return 1 +  max(left_height, right_height)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g
print(how_high(a))  # -> 3
