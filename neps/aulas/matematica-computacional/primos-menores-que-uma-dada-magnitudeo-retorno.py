n = int(input())

is_prime = [True] * (n + 1)

is_prime[0] = is_prime[1] = False

for x in range(2, n + 1):
    if not is_prime[x]:
        continue

    for i in range(x * 2, n + 1, x):
        is_prime[i] = False

for i in range(1, n + 1):
    if is_prime[i]:
        print(i, end=" ")
