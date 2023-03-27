def twoSum(nums, target):
    """
    create a hashset : empty
    iterate list
    check for complement target - i
    is complement in hashset
        return indices
    if not add to hashset
    return false
    :return: int
    """

    # brute force

    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []

    # better approach

    hashset = {}  # val -> index

    for i, num in enumerate(nums):
        if target - num in hashset:
            return [hashset[target - num], i]
        hashset[num] = i
    return []


print(twoSum([2, 11, 7, 15], 9))
