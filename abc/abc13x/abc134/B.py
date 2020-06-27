N, D = map(int, input().split())
cnt = 0

for i in range(N):
    cnt += D * 2 + 1
    if N <= cnt:
        print(i + 1)
        exit()
