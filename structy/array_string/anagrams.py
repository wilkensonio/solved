"""Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

anagrams('restful', 'fluster') # -> True
anagrams('cats', 'tocs') # -> False
anagrams('monkeyswrite', 'newyorktimes') # -> True
anagrams('paper', 'reapa') # -> False
anagrams('elbow', 'below') # -> True
anagrams('tax', 'taxi') # -> False
anagrams('taxi', 'tax') # -> False
"""

from collections import Counter


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return word_count(s1) == word_count(s2)


def word_count(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


print(anagrams('restful', 'flister'))

# print(Counter('restful') == Counter('fluster')) # Counter return a dict letter:count
