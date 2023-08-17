class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def add_lists(head_1, head_2):
	dummy_head = Node("dummy")
	tail = dummy_head
	curr_1 = head_1
	curr_2 = head_2
	carry = 0
	while curr_1 or curr_2 or carry == 1:
		val_1 = curr_1.val if curr_1 else 0
		val_2 = curr_2.val if curr_2 else 0
		
		sum = val_1 + val_2 + carry
		carry = sum // 10  if sum > 9 else 0
		digit = sum % 10
		
		tail.next = Node(digit)
		tail = tail.next
		
		if curr_1:
			curr_1 = curr_1.next
		
		if curr_2:
			curr_2 = curr_2.next
	
	return dummy_head.next

# a1 = Node(9)
# a2 = Node(8)
# a1.next = a2
# # 9 -> 8

# b1 = Node(7)
# b2 = Node(4)
# b1.next = b2

a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)
h = add_lists(a1, b1)

# while h:
#   print(h.val, end=" -> ")
#   h = h.next