i_a, i_b, f_a, f_b = map(int, input().split())

if i_b == f_b:
    if i_a == f_a:
        print("0\n")
    else:
        print("1\n")

else:
    if(i_a != f_a):
        print("1\n")
    else:
        print("2\n")

