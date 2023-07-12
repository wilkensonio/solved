"""
leaf list
Write a function, leaf_list, that takes in the root
 of a binary tree and returns a list containing the values
  of all leaf nodes in left-to-right order.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def leaf_list(root):
#   arr = []
#   _leaf_list(root, arr)
#   return arr

def leaf_list(root):
    if not root:
        return []

    if not root.right and not root.left:
        return [root.val]

    left = leaf_list(root.left)
    right = leaf_list(root.right)
    return [*left, *right]


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(leaf_list(a))  # -> [ 'd', 'e', 'f
