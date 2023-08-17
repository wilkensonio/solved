"""
most frequent char
Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

most_frequent_char('bookeeper') # -> 'e'
most_frequent_char('david') # -> 'd'

"""


def most_frequent_char(s):
    max_char, most_freq = float('-inf'), " "
    char_count = {}

    for l in s:
        char_count[l] = char_count.get(l, 0) + 1

    for ch in s:
        if max_char < char_count[ch]:
            max_char = char_count[ch]
            most_freq = ch

    return most_freq


print(most_frequent_char('bookeepeaaar'))
