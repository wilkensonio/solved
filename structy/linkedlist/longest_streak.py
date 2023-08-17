

"""
longest streak
Write a function, longest_streak, that takes in the head of a linked list as an argument.
 The function should return
the length of the longest consecutive streak of the same value within the list.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

# def longest_streak(head):
#   if not head:
#     return 0
#   streak = 1
#   curr_streak = 1
#   h1 = head
#   h2 = head.next

#   while h2:
#     if h2.val == h1.val:
#       curr_streak += 1
#     else:
#       curr_streak = 1
#     if streak < curr_streak:
#       streak = curr_streak
#     h2 = h2.next
#     h1 = h1.next
#   return streak

# def longest_streak(head):
#   if not head:
#     return 0

#   curr_streak = 0
#   streak = 0

#   h1 = head
#   h2 = head

#   while h2:
#     if h1.val == h2.val:
#       curr_streak += 1
#       h2 = h2.next
#     else:
#       h1 = h2
#       curr_streak = 0
#     if curr_streak > streak:
#       streak = curr_streak


#   return streak


def longest_streak(head, count=0):
	if not head:
		return 0
	if head.val == head.next:
		count += 1
	return longest_streak(head.next, count + 1)


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

longest_streak(a) # 3


print(longest_streak(a))