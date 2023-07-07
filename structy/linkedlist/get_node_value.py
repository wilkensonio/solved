"""
get node value
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.
"""


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
	if not head:
		return
	if index == 0:
		return head.val
	return get_node_value(head.next, index - 1)

# def get_node_value(head, index):
#   pos = -1
#   if not head:
#     return
#   cur = head
#   while cur:
#     pos += 1
#     if pos == index:
#       return cur.val
#     cur = cur.next

# def get_node_value(head, index):
#   return _get_node_value(head, index, 0)

# def _get_node_value(head, index, pos):
#   if not head:
#     return
#   if pos == index:
#     return head.val
#   return _get_node_value(head.next, index, pos + 1)
