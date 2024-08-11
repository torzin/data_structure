n1 = int(input())
p1 = input()

n2 = int(input())
p2 = input()

max_len = 0
for i in range(min(n1, n2)):
    char1 = p1[i]
    char2 = p2[i]

    if char2 == char1:
        max_len += 1
    else:
        break

print(max_len)
