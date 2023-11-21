"""
befitting brackets
Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }

"""


def befitting_brackets(string):
    stack = []
    open = ['(', '{', '[']
    close = [')', '}', ']']

    for c in string:
        if c in open:
            stack.append(c)
        elif c in close:
            if stack:
                if open.index(stack[-1]) == close.index(c):
                    stack.pop()
            else:
                return False
    return len(stack) == 0


befitting_brackets('(){}[](())')  # -> True
befitting_brackets('({[]})')  # -> True
befitting_brackets('[][}')  # -> False
befitting_brackets('{[]}({}')  # -> False
befitting_brackets('[]{}(}[]')  # -> False
befitting_brackets('[]{}()[]')  # -> True
befitting_brackets(']{}')  # -> False
befitting_brackets('')  # -> True
befitting_brackets("{[(}])")  # -> False
