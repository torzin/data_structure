txt = input().split()
espec = input()

dic = {}

for i in espec:
    dic[i] = True

global_count = 0

for i in txt:
    texto = list(i)
    for j in texto:
        try:
            if dic[j]:
                global_count += 1
                break
        except KeyError:
            continue

print(global_count)
