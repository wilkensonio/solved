"""
tree levels
Write a function, tree_levels, that takes in the root of a binary tree.
 The function should return a 2-Dimensional list where each sublist represents a level of the tree.
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_levels(root):
    result = []
    _tree_levels(root, result, 0)
    return result


def _tree_levels(root, res, level):
    if not root:
        return []

    if len(res) == level:
        res.append([root.val])
    else:
        res[level].append(root.val)

    _tree_levels(root.left, res, level + 1)
    _tree_levels(root.right, res, level + 1)


# def tree_levels(root):
#   if not root:
#     return []
#   queue = deque([(root, 0)])
#   res = []
#   while queue:
#     node, level = queue.popleft()
#     if level == len(res):
#       res.append([node.val])
#     else:
#       res[level].append(node.val)
#     if node.left:
#       queue.append((node.left, level + 1))

#     if node.right:
#       queue.append((node.right, level + 1))
#   return res


# def tree_levels(root):
#   if not root:
#     return []
#   result = []
#   stack = [(root, 0)]

#   while stack:
#     node, level = stack.pop()
#     print(len(result))
#     if level == len(result):
#       result.append([node.val])
#     else:
#       result[level].append(node.val)

#     if node.right:
#       stack.append((node.right, level + 1))

#     if node.left:
#       stack.append((node.left, level + 1))


# return result


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

print(tree_levels(a))  # ->
