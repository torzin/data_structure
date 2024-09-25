n1 = input()
n2 = input()

if len(n1) > len(n2):
    qnt_zeros = len(n1) - len(n2)
    n2 = '0' * qnt_zeros + n2
elif len(n2) > len(n1):
    qnt_zeros = len(n2) - len(n1)
    n1 = '0' * qnt_zeros + n1

n1_c = ""
n2_c = ""
for i in range(len(n1) - 1, -1, -1):

    if int(n2[i]) > int(n1[i]):
        n2_c = n2[i] + n2_c

    elif int(n2[i]) < int(n1[i]):
        n1_c = n1[i] + n1_c

    else:
        n1_c = n1[i] + n1_c
        n2_c = n2[i] + n2_c


if n1_c != "":
    n1 = int(n1_c)
else: n1 = -1

if n2_c != "":
    n2 = int(n2_c)
else: n2 = -1

if n1 > n2:
    print(n2, n1)
elif n2 > n1:
    print(n1, n2)
else:
    print(n1, n2)



