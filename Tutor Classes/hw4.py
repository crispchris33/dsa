# Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.


def zeroMover(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            #changing the position of the pointer
            nums[i], nums[j] = nums[j], nums[i]
            j += 1



nums = [1, 2, 0, 2, 1, 0, 0, 1, 1, 0]
zeroMover(nums)
print(nums)