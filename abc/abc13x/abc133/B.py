import math

N, D = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(N)]

temp = []

for i in range(N):
    for j in range(i + 1, N):
        sum = 0
        for k in range(D):
            # print(table[i][k], table[j][k])
            sum += abs(table[i][k] - table[j][k]) ** 2
        else:
            temp.append(sum)

ans = 0

for i in temp:
    if math.sqrt(i).is_integer():
        ans += 1

print(ans)
