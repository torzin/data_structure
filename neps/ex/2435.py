n = int(input())
seq = input()

count = 1
for i in range(n):

    if i == n-1:
        print(f"{count} {seq[i]}")
        break

    if seq[i + 1] != seq[i]:
        print(f"{count} {seq[i]}", end=" ")
        count = 1
    else:
        count += 1
