"""

summing squares
Write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

Given 12:

summing_squares(12) -> 3

The minimum squares required for 12 is three, by doing 4 + 4 + 4.

Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.


"""

import math


def summing_squares(n):
    return _summing_squares(n, {})


def _summing_squares(n, dp):
    if n == 0:
        return 0
    if n in dp:
        return dp[n]
    min_square = float('inf')

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        square = i * i
        min_square = min(min_square, _summing_squares(n - square, dp) + 1)
    dp[n] = min_square
    return min_square
