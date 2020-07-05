H, W, K = map(int, input().split())
table = [[i for i in input()] for _ in range(H)]
ans = 0

for h in range(1 << H):
    for w in range(1 << W):
        black = 0
        for i in range(H):
            if (h >> i) % 2 == 1:
                continue
            for j in range(W):
                if (w >> j) % 2 == 1:
                    continue
                if table[i][j] == '#':
                    black += 1
        if black == K:
            ans += 1

print(ans)
