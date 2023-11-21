"""quickest concat
Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list.

You may use words of the list as many times as needed."""


def quickest_concat(s, words):
    ans = _quickest_concat(s, words, {})
    return ans if ans != float('inf') else -1


def _quickest_concat(s, words, dp):
    if not s:
        return 0
    if s in dp:
        return dp[s]
    min_val = float('inf')
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            min_val = min(min_val, _quickest_concat(suffix, words, dp) + 1)
    dp[s] = min_val
    return dp[s]


quickest_concat('caution', ['ca', 'ion', 'caut', 'ut'])  # -> 2
quickest_concat('caution', ['ion', 'caut', 'caution'])  # -> 1
quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond'])  # -> 4
quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch'])  # ->
