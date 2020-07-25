A, B, C = map(int, input().split())
K = int(input())

for i in range(K):
    if B <= A:
        B *= 2
    else:
        if C <= B:
            C *= 2

if A < B < C:
    print("Yes")
else:
    print("No")
