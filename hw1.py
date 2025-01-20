rows = 5

for i in range(1, rows +1):
    print('*' * i)

for i in range(rows - 1, 0, -1):
    print('*' * i)


# rows = 5
# i = 0

# while i < rows:
#     i += 1
#     print('*' * i)

# i = rows - 1

# while i > 0:
#     print('*' * i)
#     i -= 1

do the diamond again with:
nested diamond or with one for loop



def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Success: {nums[i]}, {nums[j]}")
                return
    print("No solution")

nums = [2, 3, 4, 5]
target = 5
two_sum(nums, target)









