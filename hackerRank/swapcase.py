def swap_case(s):
    # return s.swapcase()
    x = ''
    for i in s:
        if i.islower():
            x += i.upper()
        else:
            x += i.lower()
    return x


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
