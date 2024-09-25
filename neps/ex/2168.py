n = int(input())
nums = input().replace(" ", "")

for i in range(1, (n // 2) + 1):
    ac_dig = int(nums[:i])
    ac_string = ""
    for j in range(n // i):
        ac_string += str(ac_dig)
        ac_dig += 1
        if ac_string == nums:
            break

    if ac_string == nums:
        print(nums[:i])
        break

