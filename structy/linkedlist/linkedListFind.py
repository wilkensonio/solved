
"""
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "d") # True

"""
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def linked_list_find(head, target):
#   if not head:
#     return False
#   if head.val == target:
#     return True
#   return linked_list_find(head.next, target)

def linked_list_find(head, target):
    cur = head
    while cur:
        if cur.val == target:
            return True
        cur = cur.next
    return False
