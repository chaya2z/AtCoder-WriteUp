from operator import itemgetter

N = int(input())
table = [[int(i) for i in input().split()] for _ in range(N)]
table.sort(key=itemgetter(1))
limit = 0

for i in table:
    limit += i[0]
    if i[1] < limit:
        print("No")
        exit()

print("Yes")
