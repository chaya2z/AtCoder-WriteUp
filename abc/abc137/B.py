K, X = map(int, input().split())
min_num = X - K + 1
max_num = X + K - 1

if min_num < -1000000:
    min_num = -1000000
if 1000000 < max_num:
    max_num = 1000000

num_list = list(range(min_num, max_num + 1))
num_list = [str(x) for x in num_list]
print(" ".join(num_list))
