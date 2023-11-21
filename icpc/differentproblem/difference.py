import sys
# func input_process -> [[]]
    # arr = []
    # for line in input
        #arr.push(line.split())
    # return arr
    
# func solution - > int
    # pair_data = input_process()
    # for elm1 elm2 in pair_data
        # ans = elm1 - elm2
        # print(abs(ans)) 
# solution()

def input_process():
    input_arr = []
    for line in sys.stdin:
        input_arr.append(line.split())
    return input_arr

def solution():
    pair_data = input_process()
    print(pair_data)
    for  a, b in pair_data:
        print(abs(int(a) - int(b)))
        
solution()

    