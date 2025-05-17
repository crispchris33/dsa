nums = [1,2,3,4,5]
    for i in nums:
        print(1)
    
x = 5
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

dictionary = {"brand": "Ford", "model": "Mustang"}
print(dictionary["brand"])

array = []
array = []



#Two Sum

# #Logic:
#     suppose nums = [2,7,11,15] and target = 9
#     initialize num_map = {}
#     start iterating:
#         for 2 (index 0):
#             diff = 9 - 2 = 7
#             add num_map = {2: 0}
#         for 11 (index 1):
#             diff = 9 - 11 = -2
#             add num_map
#         for 7 (index 1):
#             diff = 9 - 7 = 2


def two_sum(nums, targets):
    num_map = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return []

nums[2, 11, 7, 15]
target = 9
result = two_sum(nums, target)
print(result)