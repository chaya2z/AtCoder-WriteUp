from operator import itemgetter

N = int(input())
# table = [[i for i in input().split()] for j in range(N)]
table = []
for i in range(N):
    value = list(input().split())
    value[1] = int(value[1])
    value.append(str(i + 1))
    table.append(value)

point_sort = sorted(table, key=itemgetter(1), reverse=True)
alphabet_sort = sorted(point_sort, key=itemgetter(0))

for i in alphabet_sort:
    print(i[2])
