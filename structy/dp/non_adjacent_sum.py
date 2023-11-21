"""
non adjacent sum
Write a function, non_adjacent_sum, that takes in a list of numbers as an argument.
The function should return the maximum sum of non-adjacent items in the list.
There is no limit on how many items can be taken into the sum as long as they are not adjacent.
"""


def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})


def _non_adjacent_sum(nums, i, dp):
    if len(nums) <= i:
        return 0

    if i in dp:
        return dp[i]

    left = nums[i] + _non_adjacent_sum(nums, i + 2, dp)
    right = _non_adjacent_sum(nums, i + 1, dp)
    dp[i] = max(left, right)
    return dp[i]


# def find_sum(nums):
#     n = len(nums)
#     if not nums or n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
#     dp = [n] * n
#
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     for i in range(2, n):
#         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#     return dp[i]

nums = [2, 4, 5, 12, 7]
non_adjacent_sum(nums)  # -> 16
nums = [7, 5, 5, 12]
non_adjacent_sum(nums)  # -> 19
nums = [7, 5, 5, 12, 17, 29]
non_adjacent_sum(nums)  # -> 48
