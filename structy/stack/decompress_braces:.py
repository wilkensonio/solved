"""
decompress braces
Write a function, decompress_braces, that takes in a compressed string as an argument. The function should return the string decompressed.

The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times.

You may assume that every number n is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.

"""


def decompress_braces(string):
    stack = []
    for c in string:

        if c not in '})]':
            if c != '{' and c != '(' and c != '[':
                stack.append(c)
        else:
            seg = ""
            while stack[-1] and not stack[-1].isdigit():
                seg = stack.pop() + seg
            stack.append(int(stack.pop()) * seg)

    return "".join(stack)


decompress_braces("2{q}3{tu}v")
# -> qqtututuv
decompress_braces("ch3{ao}")
# -> chaoaoao
decompress_braces("2{y3{o}}s")
# -> yoooyooos
decompress_braces("z3{a2{xy}b}")
# -> zaxyxybaxyxybaxyxyb
decompress_braces("2{3{r4{e}r}io}")
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio
decompress_braces("go3{spinn2{ing}s}")
# -> gospinningingsspinningingsspinningings
decompress_braces("2{l2{if}azu}l")
# -> lififazulififazul
