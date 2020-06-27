N, K = map(int, input().split())
p_int_list = list(map(int, input().split()))
p_int_list_sorted = sorted(p_int_list)

print(sum(p_int_list_sorted[:K]))
