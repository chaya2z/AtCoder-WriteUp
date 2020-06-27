from itertools import chain, combinations

N, M, X = map(int, input().split())
table = [[int(i) for i in input().split()] for _ in range(N)]

l_2d_t = [list(x) for x in zip(*table)]


def power_set(item_lists):

    p_sets = [[]]

    for item in item_lists:
        tmp = []
        for element in p_sets:
            tmp.append(element + [item])
        p_sets.extend(tmp)

    return p_sets


tmpIndexList = power_set(range(M))
tmpIndexList = tmpIndexList[1:]
Indexes = list(range(len(tmpIndexList)))
print(Indexes)
print(tmpIndexList)


for i in range(1, M + 1):
    tmpForSumList = power_set(l_2d_t[i])
    tmpForSumList = tmpForSumList[1:]
    print(tmpForSumList)
    if sum(l_2d_t[i]) < X:
        print(-1)
        exit()
    else:
        for j in Indexes:
            if sum(tmpForSumList[j]) < X:
                Indexes.remove(j)

print(Indexes)




