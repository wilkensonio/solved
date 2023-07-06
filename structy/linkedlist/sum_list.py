"""
sum list
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19
x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

sum_list(x) # 42
"""

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
    cur = head
    res = 0
    if not cur:
        return 0
    while cur:
        res += cur.val
        cur = cur.next
    return res

def sum_list(head):
    if not head:
        return 0
    return head.val + sum_list(head.next)
