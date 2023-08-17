"""
tribonacci
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""


def tribonacci(n):
    return _tribonacci(n, {})


def _tribonacci(n, np):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    if n in np:
        return np[n]
    np[n] = _tribonacci(n - 3, np) + _tribonacci(n - 2, np) + _tribonacci(n - 1, np)
    return np[n]


print(tribonacci(14))
