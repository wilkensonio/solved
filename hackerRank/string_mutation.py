def mutate_string(string, position, character):
    s = string[:]
    s_arr = []
    for i in s:
        s_arr.append(i)
    s_arr[position] = character
    return "".join(s_arr)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
