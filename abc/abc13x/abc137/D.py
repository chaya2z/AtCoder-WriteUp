N, M = map(int, input().split())
A_B = [[int(i) for i in input().split()] for _ in range(N)]
A_B.sort(reverse=True)
A_B.sort(key=lambda x: x[1], reverse=True)

ans = 0
cnt = M

for i in range(N):
    if 0 <= cnt:
        if A_B[i][0] <= cnt:
            ans += A_B[i][1]
            cnt -= 1
    else:
        break


print(ans)
