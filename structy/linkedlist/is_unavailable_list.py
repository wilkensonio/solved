"""
is univalue list
Write a function, is_univalue_list, that takes in the head of a linked
 list as an argument. The function should return a boolean indicating
  whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.

"""

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

def is_univalue_list(head):
	curr = head
	
	while curr:
		print(curr.val)
		if head.val != curr.val:
			return False
		curr = curr.next
	return True

print(is_univalue_list(a))

a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

is_univalue_list(a)  # True

# def is_univalue_list(head, prev=None):
#   if not head:
#     return True
#   if head.val != prev and prev is not None:
#     return False
#   return is_univalue_list(head.next, head.val)

