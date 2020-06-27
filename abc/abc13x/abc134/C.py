N = int(input())
A = [int(input()) for _ in range(N)]
sort_A = sorted(A)
max_A = sort_A[-1]

for i in A:
    if max_A != i:
        print(max_A)
    else:
        print(sort_A[-2])
