import sys


def add_num(list_num):
    num1, num2 = list(map(int, list_num))
    print(num1 + num2)


for i in sys.stdin:
    arr = i.split()

add_num(arr)
