N = int(input())
monsters = list(map(int, input().split()))
heroes = list(map(int, input().split()))

damage = 0

for i in range(N):
    if monsters[i] + monsters[i + 1] <= heroes[i]:
        damage += monsters[i] + monsters[i + 1]
        monsters[i + 1] = 0
    elif monsters[i] < heroes[i]:
        damage += heroes[i]
        monsters[i + 1] -= heroes[i] - monsters[i]
    else:
        damage += heroes[i]

print(damage)
