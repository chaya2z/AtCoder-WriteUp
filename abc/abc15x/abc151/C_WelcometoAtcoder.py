N, M = map(int, input().split())
point = input().split()
thr = 0
good = 0
bad = 0

if M == 0:
    print("0 0")
else:
    for i in range(M - 1):
        if point[0] == str(thr):
            point = input().split()
            continue
        elif point[1] == "AC":
            good += 1
            thr = point[0]
            point = input().split()
            continue
        elif point[1] == "WA":
            bad += 1
            point = input().split()
            continue
    print(str(good), str(bad))
