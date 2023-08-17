"""fib
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
"""


def fib(n):
    return _fib(n, {})


def _fib(n, dp):
    if n in dp:
        return dp[n]
    if n == 1:
        return 1
    if n == 0:
        return 0

    dp[n] = _fib(n - 2, dp ) + _fib(n - 1, dp )

    return dp[n]


print(fib(46 ))
