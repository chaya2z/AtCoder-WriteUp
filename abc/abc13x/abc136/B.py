N = int(input())

if N < 10:
    print(N)
elif N < 100:
    print(9)
elif N < 1000:
    print(N - 100 + 1 + 9)
elif N < 10000:
    print(909)
elif N < 100000:
    print(N - 10000 + 1 + 909)
elif N == 100000:
    print(90909)
