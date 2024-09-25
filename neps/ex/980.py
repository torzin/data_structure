n = int(input())

cas = input().split()
p, m = cas.count('1'), cas.count('2')

ask_p = int(input())
ask_m = int(input())

if p >= ask_p and m >= ask_m:
    print('S')
else:
    print('N')