class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node(78)
b = Node(9)
c = Node(3)

a.next = b
b.next = c
c.next = None


def print_node_iter(head):  # iterative
    current = head
    while current is not None:
        print(current.value)
        current = current.next


def print_node_recur(head):
    if head is None:
        return
    print(head.value)
    print_node_recur(head.next)


# print_node_iter(a)
print_node_recur(a)


def link_to_arr(head):  # recursive
    nodes = []
    fill_list(head, nodes)
    return nodes


def fill_list(head, lst):  # helper to recursive func
    if head is None:
        return
    lst.append(head.value)
    fill_list(head.next, lst)


# def link_to_arr(head):
#     nodes = []
#     while head is not None:
#         nodes.append(head.value)
#         head = head.next
#     return nodes


# def linked_list_find(head, target):  # iterative
#     current = head
#     while current is not None:
#         if current.val == target:
#             return True
#         current = current.next
#     return False


def linked_list_find(head, target):  # recursive
    if head is None:
        return False
    if head.value == target:
        return True
    return linked_list_find(head.next, target)


# def get_node_value(head, position):
#   index = -1
#   while head is not None:
#     index += 1
#     if index == position:
#       return head.val
#     head = head.next

def get_node_value(head, index):
    pos = -1
    if head is None:
        return
    pos += 1
    if pos == index:
        return head.val
    return get_node_value(head.next, index - 1)


print(link_to_arr(a))
print(linked_list_find(a, 3))


def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


# def reverse_list(head, prev = None):
#     if head is None:
#         return prev
#     next = head.next
#     head.next = prev
#     return reverse_list(next, head)


def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0

    while current_2 is not None and current_1 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1

    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2

    return head_1


def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

    if current_1 is not None: tail.next = current_1
    if current_2 is not None: tail.next = current_2

    return dummy_head.next
