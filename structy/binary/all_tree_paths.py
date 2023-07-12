"""
all tree paths
Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

You may assume that the input tree is non-empty.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# def all_tree_paths(root):
#   stack = [(root, [root.val])]
#   array = []
#   while stack:
#     node, arr = stack.pop()
#     if not node.left and not node.right:
#       array.append(arr)
#     if node.right:
#       stack.append((node.right, arr + [node.right.val]))
#     if node.left:
#       stack.append((node.left, arr + [node.left.val]))
#   return array

def all_tree_paths(root):
    result = []
    if not root:
        return []
    if not root.left and not root.right:
        return[[root.val]]

    left = all_tree_paths(root.left)
    for arr in left:
        result.append([root.val, *arr])

    right = all_tree_paths(root.right)
    for arr in right:
        result.append([root.val, *arr])

    return result



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

print(all_tree_paths(a)) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]