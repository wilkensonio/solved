from collections import deque

"""
tree includes
Write a function, tree_includes, that takes in the root of a binary
 tree and a target value. The function should return a boolean
  indicating whether or not the value is contained in the tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes_recur(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    return (tree_includes(root.left, target)
            or tree_includes(root.right, target))


def tree_includes(root, target):  # bfs
    queue = deque([root])
    while queue:
        visited = queue.popleft()
        if target == visited.val:
            return True
        if visited.left:
            queue.append(visited.left)
        if visited.right:
            queue.append(visited.right)

    return False


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

print(tree_includes(a, "e"))
print(tree_includes_recur(a, "e"))
