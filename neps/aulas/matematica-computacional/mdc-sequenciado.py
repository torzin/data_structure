n = int(input())
nums = list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


ans = 0
if n == 2:
    ans = gcd(nums[0], nums[1])
else:
    n1 = nums[0]
    n2 = nums[1]
    ans = gcd(n1, n2)
    for i in range(2, n):
        ans = gcd(ans, nums[i])

print(ans)




