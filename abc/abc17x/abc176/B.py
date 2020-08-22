N = int(input())

if N == 0:
    print("Yes")
else:
    ans = sum(list(map(int, str(N))))
    if ans % 9 == 0:
        print("Yes")
    else:
        print("No")
