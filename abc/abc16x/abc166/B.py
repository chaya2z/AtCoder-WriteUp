N, K = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(K * 2)]

ans_list = []
sunuke_set = set(list(range(1, N + 1)))

for i in range(1, K * 2 + 1, 2):
    ans_list += table[i]

ans_set = set(ans_list)

print(len(sunuke_set - ans_set))
