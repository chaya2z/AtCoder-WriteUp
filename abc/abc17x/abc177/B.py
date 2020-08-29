import re

S = input()
T = list(input())

ans = 0
cnt = 0

for i in range(len(S) - len(T) + 1):
    cnt = 0
    for j in range(len(T)):
        # print(S[i + j], T[j])
        if S[i + j] == T[j]:
            cnt += 1
            if ans < cnt:
                ans = cnt


print(len(T) - ans)
