import math

n_nums = int(input())
nums = list(map(int, input().split()))

if list(set(nums)) != nums:
    print(0)
else:
    min_dist = math.inf
    nums = sorted(nums)

    for i in range(n_nums - 1):
        if nums[i+1] - nums[i] < min_dist:
            min_dist = nums[i+1] - nums[i]

    print(min_dist)