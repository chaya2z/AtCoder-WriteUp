W = list(input())

ans = []

for i in W:
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
        continue
    ans.append(i)

print(''.join(ans))
