def fascinating(n: int):

    if len(str(n)) != 3 or int(n) < 100 or int(n) > 999:
        return ""
    concact = str(n) + str(2 * n) + str(3 * n)
    print(concact)
    res = {x for x in concact}
    print(res)
    if len(concact) != len(res) or '0' in res:
        return False
    return True
#   # res = set()
#         # original, times_two, times_three = n, 2 * n, 3 * n
#         # concact = str(original) + str(times_two) + str(times_three)
#         # for char in concact:
#         #     if char != '0':
#         #         res.add(char)
#         # n = str(n)
#
#         # if len(n) != 3 or int(n) < 100 or int(n) > 999:
#         #     return ""
#         # else:
#         #     if len(concact) != len(res):
#         #         return False
#         #     return True


print(fascinating(100))
# 6425. Find the Longest Semi-Repetitive Substring

def longestSemiRepetitiveSubstring(s: str) -> int:
    if len(s) < 1 or len(s) > 50:
        return - 1
    if len(set(s)) == 1 and len(s) > 2:
        return 2
    i = 0
    j = 0

    output = []
    len_s = len(s) + 1
    s = s + "!"
    while len_s > 1:
        output.append(s[i])
        j += 1
        if s[i] != s[j]:
            i += 1
        else:
            i += 1
            j += 1
            output.append(s[i])
            output.append(s[j])
            break
        len_s -= 1

    return len(output)


print(longestSemiRepetitiveSubstring("1233"))
