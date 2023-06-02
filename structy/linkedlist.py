# linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')

a.next = b
b.next = c
c.next = None


def print_node_iter(head):  # iterative
    current = head
    while current is not None:
        print(current.value)
        current = current.next


def print_node_recur(head):
    current = head
    if current is None:
        return
    print(current.value)
    print_node_recur(current.next)


# print_node_iter(a)
print_node_recur(a)
