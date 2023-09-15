"""
paired parentheses
Write a function, paired_parentheses, that takes in a string as an argument.
The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains only alphabetic characters, '(', or ')'.

"""


def paired_parentheses(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


paired_parentheses("()")  # -> True
paired_parentheses("(((potato())))")  # -> True
paired_parentheses("(())(water)()")  # -> True
paired_parentheses("(())(water()()")  # -> False
paired_parentheses("")  # -> True
print(paired_parentheses("))()")) # False
