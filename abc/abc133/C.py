L, R = map(int, input().split())

num_list = list(range(L, R + 1))

num_list = [i % 2019 for i in num_list]
num_list.sort()

if 3 in set(num_list) and 673 in set(num_list):
    print(0)
else:
    print(num_list[0] * num_list[1])
