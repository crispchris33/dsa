Problem: Remove Duplicates from Sorted Array length, sorted


def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index_pointer = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index_pointer] = nums[i]
            unique_index_pointer += 1

    return unique_index_pointer

nums = [0,0,1,1,2,2,3,4,4,5]
length = remove_duplicates(nums)
print(f"Length of the array is: {length}")
print(f"Modified array: {nums[:length]}")