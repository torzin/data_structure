e = int(input()) * 2
a = int(input()) * 3
c = int(input()) * 5

total = a + e + c

if total >= 200:
    print('O')
elif 150 <= total < 200:
    print('S')
elif 100 <= total < 150:
    print('B')
else:
    print("N")
