X = int(input())

yen = 100

for i in range(3761):
    if X <= yen:
        print(i)
        exit()
    yen += yen // 100
