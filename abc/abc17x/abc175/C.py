X, K, D = map(int, input().split())

X = abs(X)

if K < X // D:
    print(X - (K * D))
    exit()
else:
    # 残りが偶数か奇数か
    if (K - X // D) % 2 == 0:
        print(X % D)
        exit()
    else:
        print(min(abs(X % D - D), abs(X % D + D)))
        exit()
