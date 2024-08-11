n = int(input())

sum = 0

for i in range(n):
    num = input()
    if len(num) == 1:
        continue

    num_lis = list(num)
    sum += int(''.join(num_lis[:-1]))**int(num_lis[-1])

print(sum)
