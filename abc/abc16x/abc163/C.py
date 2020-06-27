import collections

N = int(input())
A = list(map(int, input().split()))

A_cnt = collections.Counter(A)

for i in range(1, N + 1):
    print(A_cnt[i])
