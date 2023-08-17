x = ['a', 'b', 'c', 'z', 'a', 'c']

kn = 2


def bucketsort(nums: list[int], k: int) -> list[str]:
	count = {}
	freq = [[] for i in range(len(nums) + 1)]

	for n in nums:
		count[n] = count.get(n, 0) + 1

	for n, c in count.items():
		freq[c].append(n)

	res = []
	for i in range(len(freq) - 1, 0, -1):
		for n in freq[i]:
			res.append(n)
			if len(res) == k:
				return res


print(bucketsort(x, 2))
