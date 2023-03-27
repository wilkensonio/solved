if __name__ == '__main__':
    N = int(input())
    command = []
    for n in range(N):
        x = input().split()
        command.append(x)

    array = []
    for i in range(len(command)):
        if command[i][0] == 'append':
            array.append((int)(command[i][1]))
        elif command[i][0] == 'insert':
            array.insert((int)(command[i][1]), (int)(command[i][2]))
        elif command[i][0] == 'print':
            print(array)
        elif command[i][0] == 'remove':
            array.remove((int)(command[i][1]))
        elif command[i][0] == 'sort':
            array.sort()
        elif command[i][0] == 'pop':
            array.pop()
        elif command[i][0] == 'reverse':
            array.reverse()
