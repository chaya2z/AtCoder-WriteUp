N, L = map(int, input().split())
taste_list = list(range(L, N + L, 1))
print(sum(taste_list) - min(taste_list, key=lambda x: -x if x < 0 else x))
