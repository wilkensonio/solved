from sys import stdin

'''
 server serve O matic 1000
 always know where is it
 where it stops and where it thinks it stops
 input 100 simulation
 each simulation start w/ a room description
 which is 2 integer w and l , of rectangular room in meters
 may walk anywhere mark by the corner (0,0) to w-1, l-1

 after the room is the path the robots plain to take
 start w/ 1-n-100 num of walking segment
 each segment is given on a line as x y
 where:
 x is one of :
 u - up
 d - down
 l - left
 r - right
 y is the number of meter to move in that direction range (0,30)
 up and down move along l and left & right move along w
 up and right in positive direction
 down and left in the negative direction
 end input when l w = 0 0

 sudo:

 A : read width w and length l
 repeat A until w and l are 0

 read number of instruction n from input
 init start position (0 0)

 for each description do the following
 read direction dir , distance dist from input
 if up add dist to y-direction
 if down subtract from y-direction
 if right add dist to x-direction
 if left subtract dist from x-direction

 if x < 0 set to 0
 if x greater than w set to w
 if y < 0 set to 0
 if y greater than l set to l
 print robot x y think position
 print x y actual position
'''


def bounding_robot():

    while True:
        w, l = map(int, input().split())
        if w == 0 and l == 0:
            break

        x, y = (0, 0)  # starting position
        m, e = (0, 0)  # actual position

        for _ in range(int(input())):
            direction, distance = input().split()
            distance = int(distance)

            if direction == 'u':
                y = min(y + distance, l - 1)
                e = min(m + distance, l - 1)
                if e > l-1:
                    e = l-1
            elif direction == 'd':
                y = max(y - distance, 0)

            elif direction == 'r':
                x = min(x + distance, w - 1)
                m = min(x + distance, w - 1)
                if m > w-1:
                    m = w-1

            elif direction == 'l':
                x = max(x - distance, 0)


        print(f'Robot thinks {x} {y}')
        print(f'Actually at {m} {e}\n')


bounding_robot()
