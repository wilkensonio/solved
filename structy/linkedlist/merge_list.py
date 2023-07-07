"""
merge lists
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments.
 The function should merge the two lists together into single sorted linked list. The function
  should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


def merge_lists(head_1, head_2):
	c1, c2 = head_1, head_2
	tail = Node(None)
	head = tail
	
	while c1 and c2:
		if c1.val < c2.val:
			tail.next = c1
			c1 = c1.next
		else:
			tail.next = c2
			c2 = c2.next
		tail = tail.next
	if c1:
		tail.next = c1
	if c2:
		tail.next = c2
	
	return head.next


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

merge_lists(a, q)
