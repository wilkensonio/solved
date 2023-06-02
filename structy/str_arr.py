"""
Write a function, pair_product, that takes in a list and a target product as arguments.
The function should return a tuple containing a pair of indices whose elements multiply
 to the given target. The indices returned must be unique.
Be sure to return the indices, not the elements themselves.
There is guaranteed to be one such pair whose product is the target.
"""
# n = length of numbers list
# Time: O(n)
# Space: O(n)

def pair_product(numbers, target_product):
	hashmap = {}
	for i, num in enumerate(numbers):
		comp = target_product // numbers[i]
	if comp in hashmap:
		return tuple(hashmap[comp], i)
	hashmap[num] = i


# print(pair_product([3, 2, 5, 4, 1], 8))


'''uncompress
Write a function, uncompress, that takes in a string as
an argument. The input string will be formatted into multiple
groups according to the following pattern:
<number><char>
for example, '2c' or '3a'.
The function should return an uncompressed version of the
string where each 'char' of a group is repeated 'number'
times consecutively. You may assume that the input string is
well-formed according to the previously mentioned pattern.
uncompress("2c3a1t") # -> 'ccaaat\''''


#  n number of group
#  m max number found in any group
# time O(n * m)
# space O(n * m)


def uncompress(s):
	pointerI = 0
	pointerJ = 0
	result = []

	while pointerJ < len(s):
		if s[pointerJ].isalpha():
			i = s[pointerI: pointerJ]
			multiplier = "".join(i)
			result.append(s[pointerJ] * int(multiplier))
			pointerJ += 1
			pointerI = pointerJ
		else:
			pointerJ += 1
	return "".join(result)


# print(uncompress("1w1i1l1k1e1n1s1o1n"))  #wilkenson


'''
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where
consecutive occurrences of the same characters are compressed into the
number of occurrences followed by the character. Single character
occurrences should not be changed.
'''


# n = string length
# time O(n)
# space O(n)


def compress(s):
	s = s + " "
	# aaacc -> 3:a, 2:c
	result = []  # store compress str
	pointerI = 0
	pointerJ = 0
	count = 0  # number of char

	while pointerJ < len(s):
		if s[pointerI] == s[pointerJ]:
			count += 1
			pointerJ += 1
		else:
			if count != 1:
				result.append(str(count))
			result.append(s[pointerI])
			pointerI = pointerJ
			count = 0

	return ''.join(result)

# print(compress("nnneeeeeeeeeeeezz"))  # nnneeeeeeeeeeeezz
