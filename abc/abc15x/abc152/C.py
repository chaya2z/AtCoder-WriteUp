N = int(input())
int_list = list(map(int, input().split()))

j = 0
count = 0
good = 0

for i in range(N):
    while j <= i:
        if int_list[i] <= int_list[j]:
            if i == j and j == count:
                good += 1
            count += 1
            j += 1
        else:
            j += 1
            continue
    j = 0
    count = 0

print(good)
