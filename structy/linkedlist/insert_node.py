"""
insert node
Write a function, insert_node, that takes in the head of a
linked list, a value, and an index. The function should insert a
 new node with the value into the list at the specified index.
  Consider the head of the linked list as index 0. The function
   should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


def insert_node(head, value, index):
	new_node = Node(value)
	curr = head
	idx = 0
	while curr:
		if index == 0:
			new_node.next = curr
			return new_node
		
		if idx == index - 1:
			next_node = curr.next
			curr.next = new_node
			new_node.next = next_node
		
		curr = curr.next
		idx += 1
	return head


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'x', 2)
# a -> b -> x -> c -> d


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d


head = insert_node(a, 'v', 0)

while head:
	print(head.val)
	head = head.next
