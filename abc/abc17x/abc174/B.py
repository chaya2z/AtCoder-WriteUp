import math

N, D = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(N)]

ans = 0

for i in table:
    if math.sqrt(i[0] ** 2 + i[1] ** 2) <= D:
        ans += 1

print(ans)
