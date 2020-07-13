import collections

ans_list = []

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            tmp = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if tmp <= 10000:
                ans_list.append(tmp)

ans_list = sorted(ans_list)
print(ans_list)

N = int(input())

c = collections.Counter(ans_list)

for i in range(1, N + 1):
    print(c[i])
