A, B, C, K = map(int, input().split())

ans = 0

if A - K < 0:
    ans += A
    K -= A
    if B - K < 0:
        K -= B
        if C - K < 0:
            print(ans - C)
        else:
            print(ans - K)
    else:
        print(ans)
else:
    print(K)