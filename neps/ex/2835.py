n = int(input())

related = [['', 0] for _ in range(n)]

words = {}

for i in range(n):
    all = input().split()
    type_article, number_words, word = all[0], all[1], all[2:]
    related[i][0] = type_article
    for j in word:
        words[j] = i


qnt_words = int(input())
for i in input().split():
    try:
        related[words[i]][1] += 1
    except KeyError:
        pass

related.sort(key=lambda x: (-x[1], x[0]))
print(related[0][0])
