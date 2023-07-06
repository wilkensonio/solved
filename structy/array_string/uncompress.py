"""uncompress
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

uncompress("2c3a1t") # -> 'ccaaat'
uncompress("4s2b") # -> 'ssssbb'
"""

def uncompress(s):
    num = '0123456789'
    res = []
    i = 0
    j = 0

    while j < len(s):
        if s[j] in num:
            j += 1
        else:
            n = int(s[i:j])
            res.append(s[j] * n)
            j += 1
            i = j

    return "".join(res)


print(uncompress("14r"))