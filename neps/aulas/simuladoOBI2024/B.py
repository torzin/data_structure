ac = int(input())
m = int(input())
a = int(input())

day = 0
count = ac

while count < a:
    day += 1
    count += (count * m) + ac

print(day)