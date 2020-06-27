#  selected from AtCoder Problems recommendation
X = int(input())


if X == 1:
    print(1)
    exit()

for i in range(2, X):
    for j in range(2, X):
        print(i ** j)
        if X < i ** j and j != 2:
            print(i ** (j - 1))
            break
