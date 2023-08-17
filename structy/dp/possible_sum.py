"""
sum possible
Write a function sum_possible that takes in an amount and a list of positive numbers.
The function should return a boolean indicating whether or not it is possible to
create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""


def sum_possible(amount, numbers):
    return _sum_possible(amount, numbers, {})


def _sum_possible(amt, num, dp):
    if amt in dp:
        return dp[amt]
    if amt < 0:
        return False
    if amt == 0:
        return True

    for n in num:
        if _sum_possible(amt - n, num, dp):
            dp[amt] = True
            return dp[amt]
    dp[amt] = False
    return dp[amt]


print(sum_possible(8, [5, 12, 4]))  # -> True, 4 + 4
print(sum_possible(15, [6, 2, 10, 19]))  # -> False
print(sum_possible(13, [6, 2, 1]))  # -> True, 6 + 6 + 1
print(sum_possible(271, [10, 8, 265, 24]))  # -> False
print(sum_possible(2017, [4, 2, 10]))  # -> False
