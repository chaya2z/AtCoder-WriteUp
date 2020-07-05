N = int(input())

if 1000 - N % 1000 == 1000:
    print(0)
else:
    print(1000 - N % 1000)
