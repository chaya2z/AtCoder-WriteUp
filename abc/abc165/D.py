import math

A, B, N = map(int, input().split())

if N < B:
    ans = math.floor((A * N) / B)
    print(ans)
else:
    if B == 1:
        underB = 0
    else:
        underB = math.floor((A * (B - 1)) / B)
    eqB = 0
    eqN = math.floor((A * N) / B) - A * math.floor(N / B)
    print(max(underB, eqB, eqN))
