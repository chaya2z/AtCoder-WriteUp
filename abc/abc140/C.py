# AtCoder Beginner Contest 140
# C - Maximal Value

N = int(input())
B = list(map(int, input().split()))
ans = B[0]

for i, j in zip(B[:-1], B[1:]):
    if i <= j:
        ans += i
else:
    ans += j

print(ans)
