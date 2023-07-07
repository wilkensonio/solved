"""zipper lists
Write a function, zipper_lists, that takes in the head of
 two linked lists as arguments. The function should zipper the
  two lists together into single linked list by alternating nodes.
   If one of the linked lists is longer than the other, the resulting
    list should terminate with the remaining nodes.
    The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty."""


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
	temp = None
	curr_1 = head_1
	curr_2 = head_2
	while curr_1 and curr_2:
		next_1 = curr_1.next
		next_2 = curr_2.next
		
		curr_1.next = curr_2
		curr_2.next = next_1
		
		temp = curr_2
		
		curr_1 = next_1
		curr_2 = next_2
	
	if curr_2:
		temp.next = curr_2
	
	return head_1
a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z