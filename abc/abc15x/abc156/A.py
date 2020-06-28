N, R = map(int, input().split())

if 10 <= N:
    print(R)
else:
    print(R + 100 * (10 - N))
