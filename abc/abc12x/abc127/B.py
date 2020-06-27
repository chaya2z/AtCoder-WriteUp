r, D, x = map(int, input().split())
a = r * x -D
for _ in range(10):
    print(a)
    a = r * a - D
