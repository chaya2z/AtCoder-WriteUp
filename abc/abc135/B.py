N = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(1, N + 1):
    if cnt == 3:
        print("NO")
        exit()
    elif i != p[i - 1]:
        cnt += 1

print("YES")
