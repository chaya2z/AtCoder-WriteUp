S_list = list(input())
T_list = list(input())
cnt = 0

print(len(S_list))

for i in range(len(S_list) - 1):
    if S_list[i] != T_list[i]:
       cnt += 1

print(cnt)
