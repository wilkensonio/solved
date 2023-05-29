# n = length of string
# Time: O(n)
# Space: O(n)

"""
most frequent char
Write a function, most_frequent_char, that takes in a string as an argument.
 The function should return the most frequent character of the string.
 If there are ties, return the character that appears earlier in the string.
You can assume that the input string is non-empty.
"""


def most_frequent_char(s):
    mapper = {}
    maximum = None

    for i in range(len(s)):
        mapper[s[i]] = 1 + mapper.get(s[i], 0)

    for c in s:
        if maximum is None or mapper[c] > mapper[maximum]:
            maximum = c
    return maximum


print(most_frequent_char('riverbed'))

# n= length of string 1
# m= length of string 2
# time O(n + m)
# space O(n + m)
# linear

'''
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the
strings are anagrams. Anagrams are strings that contain the same
characters, but in any order.'''


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    str_s, str_t = {}, {}

    for i in range(len(s1)):
        str_s[s1[i]] = 1 + str_s.get(s1[i], 0)
        str_t[s2[i]] = 1 + str_t.get(s2[i], 0)

    for e in str_s:
        if str_s[e] != str_t.get(e, 0):
            return False
    return True


"""from collections import Counter

def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)"""

# print(anagrams('pp', 'oo'))


'''
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where
consecutive occurrences of the same characters are compressed into the
number of occurrences followed by the character. Single character
occurrences should not be changed.
'''


# n = string length
# time O(n)
# space O(n)


def compress(s):
    s = s + " "
    # aaacc -> 3:a, 2:c
    result = []  # store compress str
    pointerI = 0
    pointerJ = 0
    count = 0  # number of char

    while pointerJ < len(s):
        if s[pointerI] == s[pointerJ]:
            count += 1
            pointerJ += 1
        else:
            if count != 1:
                result.append(str(count))
            result.append(s[pointerI])
            pointerI = pointerJ
            count = 0

    return ''.join(result)


# print(compress("nnneeeeeeeeeeeezz"))  # nnneeeeeeeeeeeezz


'''uncompress
Write a function, uncompress, that takes in a string as
an argument. The input string will be formatted into multiple
groups according to the following pattern:
<number><char>
for example, '2c' or '3a'.
The function should return an uncompressed version of the
string where each 'char' of a group is repeated 'number'
times consecutively. You may assume that the input string is  
well-formed according to the previously mentioned pattern. 
uncompress("2c3a1t") # -> 'ccaaat\''''


#  n number of group
#  m max number found in any group
# time O(n * m)
# space O(n * m)


def uncompress(s):
    pointerI = 0
    pointerJ = 0
    result = []

    while pointerJ < len(s):
        if s[pointerJ].isalpha():
            i = s[pointerI: pointerJ]
            multiplier = "".join(i)
            result.append(s[pointerJ] * int(multiplier))
            pointerJ += 1
            pointerI = pointerJ
        else:
            pointerJ += 1
    return "".join(result)

# print(uncompress("1w1i1l1k1e1n1s1o1n"))  #wilkenson
