"""
can concat
Write a function, can_concat, that takes in a string and a list of words as arguments. The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.

You may reuse words of the list as many times as needed.


"""


def can_concat(s, words, dp={}):
    if s == '':
        return True
    if s in dp:
        return dp[s]
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            if can_concat(suffix, words):
                dp[s] = True
                return True
    dp[s] = False
    return False


can_concat("oneisnone", ["one", "none", "is"])  # -> True
can_concat("oneisnone", ["on", "e", "is"])  # -> False
can_concat("oneisnone", ["on", "e", "is", "n"])  # -> True
can_concat("foodisgood", ["is", "g", "ood", "f"])
