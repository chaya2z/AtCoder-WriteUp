#  selected from AtCoder Problems recommendation
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
h.sort(reverse=True)

ans = h[0]

for i, j in zip(h[:-K + 1], h[K - 1:]):
    div = i - j
    if div == 0:
        ans = 0
        break
    if div < ans:
        ans = div

print(ans)
