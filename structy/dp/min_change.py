"""min change
Write a function min_change that takes in an amount and a list of coins.
The function should return the minimum number of coins required to create the amount.
You may use each coin as many times as necessary.
If it is not possible to create the amount, then return -1."""


def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    return ans if ans != float('inf') else -1


def _min_change(amount, coins, dp):
    if amount in dp:
        return dp[amount]
    if amount < 0:
        return float('inf')

    if amount == 0:
        return 0

    min_coin = float('inf')

    for coin in coins:
        min_c = _min_change(amount - coin, coins, dp) + 1
        min_coin = min(min_coin, min_c)

    dp[amount] = min_coin
    return min_coin


print(min_change(8, [1, 5, 4, 12]))  # -> 2, because 4+4 is the minimum coins possible
# print(min_change(13, [1, 9, 5, 14, 30]))  # -> 5
# print(min_change(23, [2, 5, 7]))  # -> 4
# print(min_change(102, [1, 5, 10, 25]))  # -> 6
# print(min_change(200, [1, 5, 10, 25]))  # ->) 8
print(min_change(2017, [4, 2, 10]))  # -> -1
# print(min_change(271, [10, 8, 265, 24]))  # -> -1
# print(min_change(0, [4, 2, 10]))  # -> 0
# print(min_change(0, []))  # -> 0)
# print(min_change(11, [1, 2, 5]))  # -> 0)
