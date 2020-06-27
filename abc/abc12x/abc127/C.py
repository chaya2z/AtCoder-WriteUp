N, M = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(M)]

ans = [table[0][0], table[0][1]]
cnt = 0

for i in table[1:]:
    if ans[0] <= i[0] <= ans[1]:
        ans[0] = i[0]
    if ans[0] <= i[1] <= ans[1]:
        ans[1] = i[1]
    if ans[1] < i[0] or i[1] < ans[0]:
        cnt += 1
        break

if cnt != 0:
    print(0)
else:
    print(ans[1] - ans[0] + 1)
