# 136. Single Number

def unique(nums:list):
    res = 0
    for num in nums: 
        res ^= num 
    return res

print(unique([3,4,2,2,3]))