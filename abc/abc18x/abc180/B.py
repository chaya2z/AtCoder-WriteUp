import math

N = int(input())
x = list(map(int, input().split()))

m = 0
e = 0
c = 0

for i in x:
    m += abs(i)
    e += abs(i) ** 2
    c = max(c, abs(i))

print(m)
print(math.sqrt(e))
print(c)
