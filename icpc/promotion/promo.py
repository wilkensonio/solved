#   https://open.kattis.com/problems/promotions

from collections import defaultdict 
import sys 

# topological sorting 
def top_sort(graph): 
    def dfs(node):
        visited[node] = True # add current node to visited 
        for neighbor in graph[node]: # recursively visit all neighbors of current 
            if not visited[neighbor]:
                dfs(neighbor)
        topological_order.append(node) # add current node to the topological order
     
    n = max(graph) + 1   
    visited = [False] * n  # keep track of vivisted node (deault false)
    
    topological_order = []  # sort the topological order (default empty) 

    for i in range(n):  # iterate through all node in the graph 
        if not visited[i] and i in graph:  # if node no in visited start dfs in that node 
            dfs(i) 
    return topological_order[::-1]
   
# compute promotions 
def promotions(interval_start, interval_end, num_employee, rules): 
    ''' interval [a, b] num_emplyee:int num_rules/precedence : int rules: tuples'''
    graph = defaultdict(list)
    n_degree = [0] * num_employee  # keep track of n_degrees of employes
    
    for a, b in rules:  # populate graph base on precedence rules   
        graph[a].append(b)   # employee 'a' precedes employee 'b' 
        n_degree[b] += 1  # increment in_degree of 'b'
    
    print(graph)
    print(n_degree)
    top_order = top_sort(graph)  # topological order employees -> [int]
 
    # compute number of emp that is certained to be promoted for each interval [a, b]
    def compute_promotion(interval1, interval2):
        # emp up to num of promotions interval 1 and 2
        guarantee = [e for e in top_order if n_degree[e] == 0] # no dependence 
        promotion1 = top_order[:interval1]  
        promotion2 = top_order[:interval2]
        no_promotion = len(top_order) 
        num_emp_to_promote1 = 0
        num_emp_to_promote2 = 0 
        eligible = set() # eligible may get promoted
       
        # hangle interval a promotion less than quarantee 
        if len(guarantee) > interval1 and len(guarantee) <=interval2 :
            eligible_emp(guarantee, eligible)  # eligible emp no promotion guarantee
            promoted = len(guarantee) + len(eligible) # may be promted 
            p2 = len(promotion2)
            
            while promoted < p2:
                p2 -= 1
                promotion2 = promotion2[:-1] # promo 2 num emp  is more than guarantee and eligible
                num_emp_to_promote2 = len(promotion2) # update num of promotion for interval b
                no_promotion = no_promotion - promoted # update no promotion 
                
            print(num_emp_to_promote1, num_emp_to_promote2, no_promotion, sep='\n')
            
        # if in_degree is zero emp is guarantee to be promoted
        if len(guarantee) <= len(promotion1):
            for i in range(len(promotion1) -1 , 0 , -1):
                if n_degree[promotion1[i]] != 0:  
                    promotion1 = promotion1[:-1] # remove employee that depend on others
                else:
                    if len(promotion1) > interval1:
                        num_emp_to_promote1 = 0
                    break  

            eligible_emp(guarantee, eligible)
            
            num_emp_to_promote1 = len(promotion1)
            num_emp_to_promote2 = len(promotion2) 
            
            promo_left = num_emp_to_promote2 - num_emp_to_promote1
            
            while promo_left > len(eligible):
                num_emp_to_promote2 -= 1
                promo_left -= 1
                
            no_promotion = no_promotion - num_emp_to_promote2 
            print(num_emp_to_promote1, num_emp_to_promote2, no_promotion, sep='\n') 

    def eligible_emp(guarantee, eligible):
        for emp in guarantee: # emp that are not guarantee promtion but are eligible
            eligible.update(set(graph[emp]))

    compute_promotion(interval_start, interval_end)
    

# read input
interval_start, interval_end, num_emp, num_rules = map(int, sys.stdin.readline().split())
rules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_rules)]

promotions(interval_start, interval_end, num_emp, rules)
#  =========================================================
 