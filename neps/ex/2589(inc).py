import math

queries = int(input())


for _ in range(queries):
    heights = list(map(int, input().split()))

    max_height = math.inf

    ans = 0

    for idx, ac in enumerate(heights):

        other_val = max(heights[idx:])

        if other_val < max_height:
            max_height = other_val

        ans += max_height - ac

    print(ans)



