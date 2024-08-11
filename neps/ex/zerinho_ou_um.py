A, B, C = map(int, input().split())

if A == B == C:
    print('*')
elif A != B and A != C:
    print('A')
elif B != A and B != C:
    print('B')
else:
    print('C')