"""
nesting score
Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:

[] is worth 1 point
XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
[S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
You may assume that the input only contains well-formed square brackets.



"""


def nesting_score(string):
    stack = [0]
    for c in string:
        if c == '[':
            stack.append(0)
        else:
            val = stack.pop()
            if val == 0:
                stack.append(1 + stack.pop())
            else:
                stack.append(2 * val + stack.pop())
    return stack[-1]


nesting_score("[][][]")  # -> 3
nesting_score("[[]]")  # -> 2
nesting_score("[[][]]")  # -> 4
nesting_score("[[][][]]")  # -> 6
nesting_score("[[][]][]")  # -> 5
nesting_score("[][[][]][[]]")  # -> 7
nesting_score("[[[[[[[][]]]]]]][]")  # -> 129
