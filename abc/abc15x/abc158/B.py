N, A, B = map(int, input().split())

ans = N // (A + B) * A
surplus = N % (A + B)
if A < surplus:
    ans += A
    print(ans)
else:
    ans += surplus
    print(ans)
