# tree path_finder
# Write a function, path_finder, that takes in the root of a binary
# tree and a target value. The function should return an array representing
# a path to the target value. If the target value is not found in the tree, then return None.
#
# You may assume that the tree contains unique values.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def path_finder(root, target):
#     if not root:
#         return None
#     if root.val == target:
#         return [root.val]
#
#     left = path_finder(root.left, target)
#     right = path_finder(root.right, target)
#
#     if left:
#         return [root.val, *left] # not the best
#     if right:
#         return [root.val, *right] # not the best
#
#     return None
def path_finder(root, target):
    stack = [(root, [root.val])]

    while stack:
        node, path = stack.pop()

        if node.val == target:
            return path

        if node.right:
            stack.append((node.right, path + [node.right.val]))  # not thr best sol
        if node.left:
            stack.append((node.left, path + [node.left.val]))

    return None

# def path_finder(root, target):
#   result = _path_finder(root, target)
#   if result is None:
#     return None
#   else:
#     return result[::-1]


# def _path_finder(root, target):
#   if not root:
#     return None
#   if root.val == target:
#     return [root.val]
#   left_path = _path_finder(root.left, target)
#   if left_path:
#     left_path.append(root.val)
#     return left_path

#   right_path = _path_finder(root.right, target)
#   if right_path:
#     right_path.append(root.val)
#     return right_path
#   return None


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

print(path_finder(a, 'e'))
