A, B, C, D = map(int, input().split())

for i in range(max(A, C)):
    C -= B
    if C <= 0:
        print('Yes')
        exit()
    A -= D
    if A <= 0:
        print('No')
        exit()
