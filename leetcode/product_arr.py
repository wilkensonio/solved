def productExceptSelf(nums: list[int]) -> list[int]:

    length = len(nums)
    res = [1] * length
    preI = 1
    postI = 1
    i = 0
    while length > i:
        res[i] *= preI
        preI *= nums[i]
        res[length - i - 1] *= postI
        postI *= nums[length - i - 1]
        i += 1
    return res


print(productExceptSelf([1, 2, 3, 4]))
