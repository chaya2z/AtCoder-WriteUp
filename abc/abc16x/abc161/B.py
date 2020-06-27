N, M = map(int, input().split())
B = list(map(int, input().split()))

count = 0
x = 4 * M
v = sum(B) / x

for i in B:
    if i >= v:
        count += 1

if count >= M:
    print("Yes")
else:
    print("No")
