"""
linked list values
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
x = Node("x")
y = Node("y")

x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# def linked_list_values(head):
#   cur = head
#   res = []
#   while cur:
#     res.append(cur.val)
#     cur = cur.next
#   return res

# def linked_list_values(head):
#   if not head:
#     return []
#   return [head.val] + linked_list_values(head.next)


def linked_list_values(head):
    res = []
    _linked_list_values(head, res)
    return res

def _linked_list_values(head, res):
    if not head:
        return
    res.append(head.val)
    _linked_list_values(head.next, res)


print(linked_list_values(a))

