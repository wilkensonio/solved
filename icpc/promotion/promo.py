# https://open.kattis.com/problems/promotions

import sys
# s2
def build_graph(): 
    graph = {
        'A':['B','E'],
        'B':['C','F'],
        'C':['D'],
        'D':[],
        'E':['F'],
        'F':['C'],
        'G':['E'],
    }  
    return graph

# s1 read input std
def interval() -> [[str, str]]:
    interval_list= [] 
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
    children = set() # children nodes 
    key_node = set(graph.keys()) # all node 
    all_neigbors = [] # all neigbor node
    
    for node in graph:
        all_neigbors.append(graph[node])

    # find all children  
    for node in graph:
        for neigh in all_neigbors: 
            if node in neigh:
              children.add(node)
    root : set = key_node - children
    # s4
    depth_Emp : dict[set] = {}
    for r in root:
        for emp, depth in find_depth(r, graph).items(): 
            depth_Emp.setdefault(depth,  set()).add(emp)
                
    return depth_Emp 
 
#s4 find depth
def find_depth(root, graph):
    if not root:
        return 0
    distance_graph = {}
    stack = [(root, 0)] 
    visited = set(root)
    while stack:
        node, depth = stack.pop()     
        distance_graph[node] = depth
        for neigh in graph[node]:
            if neigh not in visited:
                stack.append((neigh, depth + 1))
                visited.add(neigh)
    return distance_graph 
 

def solution() -> ([], set(), set()):
    promoted = []
    intervals: [[str, str]] = interval() 
    dist_emp : dict[int, set[str]] =  find_dist_from_roots() 
    all_emp = set(dist_emp.keys()) 
    visited = {} 
    
    ab : [[int, int]] = [] # list of intervals
    for interv in intervals:
        ab.append(list(map(int, interv)))
    print(ab)
    return dist_emp
    
print(solution())


