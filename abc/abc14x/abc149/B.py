A, B, K = map(int, input().split())

if A + B - K < 0:
    print(0, 0)
elif A - K < 0:
    print(0, A + B - K)
else:
    print(A - K, B)
