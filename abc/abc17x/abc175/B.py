import itertools

N = int(input())
L_int_list = list(map(int, input().split()))
L_int_set = set(L_int_list)

ans = 0

if len(L_int_set) < 3:
    print(ans)
    exit()

for i in itertools.combinations(L_int_list, 3):
    if len(set(i)) == 3:
        if max(i) < sum(i) - max(i):
            ans += 1

print(ans)
