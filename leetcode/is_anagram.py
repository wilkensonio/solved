def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
     check length
     create hashmap
     add k, v to hashmap
     loop over hashmap
        keep count
        if count same = true
        else false
    ps. key may not exist to avoid error
    instead of saying 1 + countT[t[i], 0]
    use 1 + countT.get(t[i], 0) the get method would try getting
    the key if it doesn't exist it'll set the default to 0
    """
    #
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for j in countS:
        if countS[j] != countT.get(j, 0):
            return False
    return True


# print(isAnagram('asananannn', 'annanatnna'))
