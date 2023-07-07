from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum_dfs(root, result=0):
    stack = [root]
    while stack:
        current = stack.pop()
        result += current.val

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result


def tree_sum_dfs_recursive(root):
    if not root:
        return 0
    return root.val + tree_sum_dfs_recursive(root.left) + tree_sum_dfs_recursive(root.right)


def tree_sum_bfs(root, result=0):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result += current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


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

print(tree_sum_dfs(a))  # 21
print(tree_sum_bfs(a))  # 21
print(tree_sum_dfs_recursive(a))  # 21
