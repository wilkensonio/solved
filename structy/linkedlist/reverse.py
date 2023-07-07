"""
reverse list
Write a function, reverse_list,
 that takes in the head of a linked list as an argument.
  The function should reverse the order of the nodes in the
  linked list in-place and return the new head of the reversed linked list.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def reverse_list(head):
	prev = None
	curr = head
	
	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev


# def reverse_list(head, prev=None):
#   if not head:
#     return prev
#   next = head.next
#   head.next = prev
#   return reverse_list(next, head)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

reverse_list(a)  # f -> e -> d -> c -> b -> a
