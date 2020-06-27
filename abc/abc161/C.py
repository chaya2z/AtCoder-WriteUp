N, K = map(int, input().split())
store = N
x = N % K
if N == 0:
    print(0)
else:
    while x < store:
        store = x
        x = abs(x - K)

    if store > abs(N - K):
        print(abs(N - K))
    else:
        print(store)
