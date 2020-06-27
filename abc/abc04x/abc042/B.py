#  selected from AtCoder Problems recommendation
N, L = map(int, input().split())
table = [input() for _ in range(N)]
table.sort()

print("".join(table))
