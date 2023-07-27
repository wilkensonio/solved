def list_sum(nums: list):
	if not nums:
		return 0
	return nums[0] + list_sum(nums)


print(list_sum([]))


def list_sum(nums: list):
	if len(nums) == 1:
		return nums[0]
	else:
		return nums[0] + list_sum(nums[1:])


print(list_sum([1, 5, 6]))


def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)


def fib(n):
	seq = [0, 1]
	while len(seq) < n:
		next_v = seq[-1] + seq[-2]
		seq.append(next_v)
	return seq


print(fib(5))


def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)


def tower_of_hanoi(n, source, auxiliary, destination):
	if n == 1:
		print(f"Move disk 1 from {source} to {destination}")
		return
	tower_of_hanoi(n - 1, source, destination, auxiliary)
	tower_of_hanoi(n - 1, source, destination, auxiliary)
	tower_of_hanoi(n - 1, auxiliary, source, destination)


# Example usage:
tower_of_hanoi(3, 'A', 'B', 'C')
print(factorial(0))


class Node:
	def __init__(self, value):
		self.val = value
		self.next = None


node1 = Node(20)
node2 = Node(56)
node3 = Node(10)
node4 = Node(78)
node5 = Node(8)
node6 = Node(78)
node7 = Node(90)
node8 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8


def print_list(head):
	cur = head
	while cur:
		print(cur.val, end=' -> ')
		cur = cur.next
	print(None)


# def del_item(head, val):

#     if not head:
#         return None

#     if head.val == val:
#         return del_item(head.next, val)

#     head.next = del_item(head.next, val)
#     return head

# print_list(node1)


def remove_elm(head, k):
	if not head:
		return None
	
	cur, prev = head, None
	
	while head and head.val == k:
		head = head.next
	
	while cur:
		if cur.val == k:
			if prev:
				prev.next = cur.next
			else:
				head = cur.next
		else:
			prev = cur
		cur = cur.next
	
	return head


h = remove_elm(node1, 10)
print_list(h)
