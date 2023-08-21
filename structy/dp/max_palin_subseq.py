"""
max palin subsequence
Write a function, max_palin_subsequence, that takes in a string as an argument.
The function should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string,
while maintaining the relative order of characters.
"""


def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {})


def _max_palin_subsequence(string, i, j, dp):
    key = (i, j)
    if i > j:
        return 0
    if i == j:
        return 1
    if string[i] == string[j]:
        dp[key] = _max_palin_subsequence(string, i + 1, j + 1, dp) + 2
    else:
        dp[key] = max(
            _max_palin_subsequence(string, i + 1, j, dp),
            _max_palin_subsequence(string, i, j - 1, dp)
        )
    return dp[key]


print(max_palin_subsequence("luwxult"))
