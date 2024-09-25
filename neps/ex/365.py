n, q = map(int, input().split())

upper = input().split()
bottom = input().split()

nums = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().split())

    l -= 1

    nums[l] += 1
    nums[r] += -1

ac = 0

for i in range(n):
    if nums[i] > 0:
        ac += nums[i]

    if nums[i] < 0:
        ac += nums[i]

    if ac % 2 == 0:
        print(upper[i], end=" ")

    else:
        print(bottom[i], end=" ")
