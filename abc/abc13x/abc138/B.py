import math

N = int(input())
A = list(map(int, input().split()))

a = A[0]

for i in range(1, N):
    a = (a * A[i]) // math.gcd(a, A[i])

b = 0

for i in range(N):
    b += a // A[i]

print(a / b)
