"""
remove node
Write a function, remove_node, that takes in the head of a linked
 list and a target value as arguments. The function should delete the
  node containing the target value from the linked list and return the
   head of the resulting linked list. If the target appears multiple times.
    in the linked list, only remove the first instance of the target in the list.

Do this in-place.

You may assume that the input list is non-empty.

You may assume that the input list contains the target.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# def remove_node(head, target_val):
#   prev = Node(None)
#   curr = head

#   if head.val == target_val or not head:
#     return head.next or None

#   while curr:
#     if curr.val == target_val:
#       prev.next = curr.next
#       return head
#     prev = curr
#     curr = curr.next

def remove_node(head, target_val):
	if not head or head.val == target_val:
		return None or head.next
	head.next = remove_node(head.next, target_val)
	return head



node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4

# a -> b -> c -> d -> e -> f

x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

# x -> y -> z

remove_node(x, "z")

print(remove_node(node1, "i"))