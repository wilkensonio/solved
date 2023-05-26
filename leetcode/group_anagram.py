from collections import defaultdict
def group_anagram(strs):
    HashMap = defaultdict(list)     # mapping char count to list od anagrams
    for word in strs:
        count = [0] * 26  # a to z
        for letter in word:
            count[ord(letter) - ord('a')] += 1
        HashMap[tuple(count)].append(word)
    print(HashMap.values(), HashMap)


group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"])
