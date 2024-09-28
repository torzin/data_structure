n = int(input())

pass_words = [input() for _ in range(n)]

pass_words.sort(key=lambda x: len(x), reverse=True)

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue

        if pass_words[j] in pass_words[i]:
            if pass_words[j] == pass_words[i]:
                cnt += 1
            cnt += 1

print(cnt)