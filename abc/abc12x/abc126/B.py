# S=input()
# if int(S[:2])

s = int(input())
print(['NA', 'MMYY', 'YYMM', 'AMBIGUOUS'][(9 < s < 1000) - (0 < s % 100 < 13) * 2])
