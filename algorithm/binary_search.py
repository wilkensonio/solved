# Binary search
'''step 0:
      define a function that takes in 2 parameters, a sorted array and target number
step 1:
      assign the first and last index of the elements in the array to a variable
step 2:
    create a while loop that loops as long as start index <= end index
        identify the midpoint index from the arr
        return midpoint(index) if the mid elm = the target
        if not check that if less then target and increment start index
        else increment end index
    if target is not found
    return -1
'''


def binary_search(arr: list, target: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


sorted_array = [4, 5, 6, 7, 8, 9, 10, 89, 90, 100]
index_target = binary_search(sorted_array, 90)
print(index_target)
