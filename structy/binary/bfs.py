"""
breadth first values
Write a function, breadth_first_values, that takes in the root of a binary tree.
 The function should return a list containing all values of the tree in breadth-first order.


"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root, result: list):
    queue = deque([root])
    while queue:
        visited = queue.popleft()
        result.append(visited.val)
        if visited.left:
            queue.append(visited.left)
        if visited.right:
            queue.append(visited.right)
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

print(bfs(a, []))
