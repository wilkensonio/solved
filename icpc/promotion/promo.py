# # https://open.kattis.com/problems/promotions


import sys

# s2
roots = set()


def build_graph():
    graph = {
        'A': ['B', 'E'],
        'B': ['C', 'F'],
        'C': ['D'],
        'D': [],
        'E': ['F'],
        'F': ['C'],
        'G': ['E'],
    }
    return graph


# s1 read input std
def interval() -> [[str, str]]:
    interval_list = []
    for i in sys.stdin:
        interval_list.append([i.strip()])
    first_interval, rest = interval_list[:1], interval_list[1:]
    fr = first_interval[0]
    arr_fr = "".join(fr)
    intervals = [arr_fr.split()[:2]]
    for arr in rest:
        intervals.append("".join(arr).split())
    return intervals


# s3
def find_dist_from_roots():
    graph = build_graph()
    children = set()  # children nodes
    key_node = set(graph.keys())  # all node
    all_neigbors = []  # all neigbor node

    for node in graph:
        all_neigbors.append(graph[node])

    # find all children  
    for node in graph:
        for neigh in all_neigbors:
            if node in neigh:
                children.add(node)
    global roots
    roots = key_node - children
    # s4
    depth_Emp: dict[int, set[str]] = {}
    for root in roots:
        for emp, depth in find_depth(root, graph).items():
            depth_Emp.setdefault(depth, set()).add(emp)

    return depth_Emp


# s4 find depth
def find_depth(root, graph):
    if not root:
        return 0
    distance_graph = {}

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        distance_graph[node] = depth
        for neigh in graph[node]:
            stack.append((neigh, depth + 1))
    return distance_graph


def solution():
    intervals: [[str, str]] = interval()
    dist_emp: dict[int, set[str]] = find_dist_from_roots()

    interval_ab: [[int, int]] = []  # list of intervals
    for interv in intervals:
        interval_ab.append(list(map(int, interv)))

    def find_num_promotion(distEmp):
        promoted = []
        curr_promo = 0
        for ab in interval_ab:
            d = 0  # dist employee set  1 0 1
            i = 0  # access interval 1
            promo = ab[i]  # number of promotion 3 1 4 2 0
            Emp_to_be_promoted = len(distEmp[d])
            while i < len(ab):
                promotion = promo - Emp_to_be_promoted

                if promotion >= 0:
                    promo = promotion
                    curr_promo += Emp_to_be_promoted
                    d += 1
                else:
                    promoted.append(curr_promo)
                    curr_promo = 0
                    i += 1
                    d = 0

        return promoted

    return find_num_promotion(dist_emp)


print(solution())
