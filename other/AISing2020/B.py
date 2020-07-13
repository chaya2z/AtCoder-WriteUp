N = int(input())
a_int_list = list(map(int, input().split()))

ans = 0

for i in range(0, N, 2):
    if a_int_list[i] % 2 == 1:
        ans += 1

print(ans)
