import collections

N = int(input())
table = [input() for _ in range(N)]

cnt = collections.Counter(table)
print(cnt.most_common()[0][0])
