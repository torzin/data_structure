n = int(input())

sweet = 0
total_d = n

for i in range(n):
    type = input()

    total_d -= 1
    if type == 'sweet':
        sweet += 1
        if sweet == 2:
            if total_d == 0:
                sweet = 0
            break
    else:
        sweet = 0

if sweet == 2:
    print('No')
else:
    print('Yes')
