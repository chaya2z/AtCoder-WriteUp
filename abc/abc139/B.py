A, B = map(int, input().split())

for i in range(1, 1000000):
    if B <= (A * i) - (i - 1):
        print(i)
        exit()



