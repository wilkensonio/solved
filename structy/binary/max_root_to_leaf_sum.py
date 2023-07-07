"""
max root to leaf running_sum sum
Write a function, max_running_sum, that takes in the root of a
 binary tree that contains number values. The function should
  return the maximum sum of any root to leaf running_sum within the tree.

You may assume that the input tree is non-empty.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path_sum(root):
    if not root:
        return float('-inf')
    if not root.left and not root.right:
        return root.val
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


def max_running_sum(root):
    if not root:
        return float('-inf')

    max_sum = float('-inf')
    stack = [(root, root.val)]
    while stack:
        node, running_sum = stack.pop()

        if not node.left and not node.right:
            max_sum = max(max_sum, running_sum)

        if node.right:
            stack.append((node.right, running_sum + node.right.val))
        if node.left:
            stack.append((node.left, running_sum + node.left.val))

    return max_sum


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

print(max_running_sum(a))
print(max_path_sum(a))
# print(max_running_sum_recur(a))
