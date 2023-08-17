"""compress
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.

compress('ccaaatsss') # -> '2c3at3s'
compress('ssssbbz') # -> '4s2bz'"""

def compress(s):
    s += " "
    res = []
    counter = 0
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            counter += 1
            j += 1
        else:
            counter = j - i
            if counter > 1:
                res.append(str(counter))
                res.append(s[i])
            else:
                res.append(s[i])
            i = j

    return ''.join(res)


print(compress('ccaaatsss'))