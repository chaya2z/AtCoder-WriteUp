N = int(input())
W = list(map(int, input().split()))
ans = 10000

for i in range(1, N):
    temp_abs = abs(sum(W[:i]) - (sum(W) - sum(W[:i])))
    if temp_abs < ans:
        ans = temp_abs

print(ans)
