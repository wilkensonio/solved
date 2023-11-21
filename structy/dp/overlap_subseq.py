"""
overlap subsequence
Write a function, overlap_subsequence, that takes in two strings as arguments. The function should return the length of the longest overlapping subsequence.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.


"""


def overlap_subsequence(string_1, string_2):
    return _overlap_subsequence(string_1, string_2, 0, 0, {})


def _overlap_subsequence(string_1, string_2, i, j, dp):
    key = (i, j)
    if key in dp:
        return dp[key]
    if i == len(string_1) or j == len(string_2):
        return 0

    max_val = 0
    if string_1[i] == string_2[j]:
        max_val += _overlap_subsequence(string_1, string_2, i + 1, j + 1, dp) + 1
    else:
        max_val += max(
            _overlap_subsequence(string_1, string_2, i, j + 1, dp),
            _overlap_subsequence(string_1, string_2, i + 1, j, dp)
        )
    dp[key] = max_val
    return max_val


overlap_subsequence("dogs", "daogt")  # -> 3
overlap_subsequence("xcyats", "criaotsi")  # -> 4
overlap_subsequence("xfeqortsver", "feeeuavoeqr")  # -> 5
overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave")  # -> 11
overlap_subsequence(
    "mumblecorebeardleggingsauthenticunicorn",
    "succulentspughumblemeditationlocavore"
)
