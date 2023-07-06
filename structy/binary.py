from collections import deque


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


a = Node('A')
c = Node('C')
b = Node('B')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#              a
#             /  \
#           b      c
#          / \      \
#          d  e      f


def tree_includes(root, target):
	if not root:
		return False
	stack = [root]
	while stack:
		curr = stack.pop()
		if curr.val == target:
			return True
		if curr.left:
			stack.append(curr.left)
		if curr.right:
			stack.append(curr.right)
	
	return False


# print(tree_includes(a, 'E'))


def depth_first_values(root):
	if not root:
		return []
	result = list()
	stack = [root]
	while stack:
		current = stack.pop()
		result.append(current.val)
		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)
	return result


# print(depth_first_values(a))


def dfs_values(root: Node) -> list[str]:
	if root is None:
		return []
	left_val = dfs_values(root.left)
	right_val = dfs_values(root.right)
	return [root.val, *left_val, *right_val]


def bfs_values(root: Node):
	if not root:
		return []
	queue = deque([root])
	res = []
	while queue:
		current = queue.popleft()
		res.append(current.val)
		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	
	return res


# print(bfs_values(a))
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


def tree_sum(root):
	if not root:
		return 0
	
	res = 0
	stack = [root]
	while stack:
		curr = stack.pop()
		res += curr.val
		
		if curr.left:
			stack.append(curr.left)
		if curr.right:
			stack.append(curr.right)
	return res


# print(tree_sum(a))

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


def tree_min_value(root):
	min_val = float('inf')
	stack = [root]
	
	while stack:
		curr = stack.pop()
		if curr.val < min_val:
			min_val = curr.val
		if curr.left:
			stack.append(curr.left)
		if curr.right:
			stack.append(curr.right)
	return min_val


# print(tree_min_value(a))

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


def max_path_sum(root):
	if not root:
		return float('-inf')
	if not root.left and not root.right:
		return root.val
	return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


# print(max_path_sum(a))

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


def path_finder(root, target):
	res = _path_finder(root, target)
	if not res:
		return None
	else:
		
		return res[::-1]


def _path_finder(root, target):
	if not root:
		return None
	if root.val == target:
		return [root.val]
	
	left_arr = _path_finder(root.left, target)
	if left_arr:
		left_arr.append(root.val)
		return left_arr
	
	right_arr = _path_finder(root.right, target)
	if right_arr:
		right_arr.append(root.val)
		return right_arr
	return None


print(path_finder(a, 'e'))


# def tree_value_count(root, target):
#   if not root:
#       return 0
#   match = 1 if root.val == target else 0
#   return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)

def tree_value_count(root, target):
	if not root:
		return 0
	queue = deque([root])
	count = 0
	while queue:
		curr = queue.popleft()
		if curr.val == target:
			count += 1
		
		if curr.left:
			queue.append(curr.left)
		if curr.right:
			queue.append(curr.right)
	return count
