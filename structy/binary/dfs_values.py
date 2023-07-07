"""
depth first values
Write a function, depth_first_values, that takes in the root
 of a binary tree. The function should return a list containing
  all values of the tree in depth-first order.

Hey. This is our first binary tree problem, so you should be
liberal with watching the Approach and Walkthrough.
 Be productive, not stubborn. -AZ
 
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


# def depth_first_values(root):
#   if not root:
#     return []
#   result = []
#   stack = [root]

#   while stack:
#     cur = stack.pop()
#     if cur:
#       result.append(cur.val)

#     if cur.right:
#       stack.append(cur.right)
#     if cur.left:
#       stack.append(cur.left)

#   return result

def depth_first_values(root, values):
	stack = [root]
	while stack:
		current = stack.pop()
		values.append(current.val)
		
		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)
	
	return values


def dfs(root):
	if not root:
		return []
	left = dfs(root.left)
	right = dfs(root.right)
	return [root.val, *left, *right]


a = Node('a')
c = Node('c')
f = Node('f')
dt = Node('dot')
d = Node('d')
z = Node('z')

a.left = c
a.right = d
c.left = f
c.right = dt
d.left = z

 

