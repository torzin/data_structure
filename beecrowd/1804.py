nums = int(input())
bit = [0] * (nums + 1)


nlis = [0] + list(map(int, input().split()))
ans = 0


def setbit(pos, diff):
    while pos <= nums+1:
        bit[pos] += diff
        pos += pos & -pos


def getbit(pos):
    new_ans = 0
    while pos:
        new_ans += bit[pos]
        pos -= pos & -pos
    return new_ans


for i in range(1, nums+1):
    setbit(i, nlis[i])


while True:
    try:
        char, number = input().split()
        number = int(number)

        match char:
            case "a":
                setbit(number, -nlis[number])
            case "?":
                ans = getbit(number-1)
                print(ans)

    except EOFError:
        break

