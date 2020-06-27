N, M = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(M)]
on_off = list(map(int, input().split()))


ans_list = []

for i in range(M):
    switches = sum(table[i]) - table[i][0]
    sw_num = switches // 2
    sw_num_amari = switches % 2
    if on_off[i] == 0:
        ans_list.append(sw_num)
    else:
        ans_list.append(sw_num + sw_num_amari)

ans = 1
for i in ans_list:
    ans *= i

print(ans)
