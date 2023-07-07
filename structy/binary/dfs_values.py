"""
depth first values
Write a function, depth_first_values, that takes in the root
 of a binary tree. The function should return a list containing
  all values of the tree in depth-first order.

Hey. This is our first binary tree problem, so you should be
liberal with watching the Approach and Walkthrough.
 Be productive, not stubborn. -AZ
 
"""


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

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

def depth_first_values(root, values=[]):
	if not root:
		return []
	left = depth_first_values(root.left)
	right = depth_first_values(root.right)
	return [root.val, *left, *right]
