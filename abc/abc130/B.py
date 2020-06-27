N, X = map(int, input().split())
L = list(map(int, input().split()))

ans = 0

for i in range(N + 1):
    if sum(L[:i]) <= X:
        ans += 1
    else:
        break

print(ans)
