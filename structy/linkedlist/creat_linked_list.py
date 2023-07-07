"""
create linked list
Write a function, create_linked_list, that takes in a list of values as an argument.
The function should create a linked list containing each item of the list as the values
 of the nodes. The function should return the head of the linked list.


"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


def create_linked_list(values: list):
	if not values:
		return None
	
	head = Node(values[0])
	curr = head
	
	for node in values[1:]:
		curr.next = Node(node)
		curr = curr.next
	return head


head = create_linked_list(["h", "e", "y"])


#
# recursive 
def create_linked_list(values, i=0):
	if not values or len(values) == i:
		return None
	head = Node(values[i])
	head.next = create_linked_list(values, i + 1)
	return head
