K = int(input())
N, M = map(int, input().split())

if K == 1:
    print("OK")
    exit()

for i in range(N, M + 1):
    if (i / K).is_integer():
        print("OK")
        exit()


print("NG")
