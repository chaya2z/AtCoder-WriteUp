N = int(input())
d = list(map(int, input().split()))
d.sort()
div = N // 2 - 1

print(d[div + 1] - d[div])

