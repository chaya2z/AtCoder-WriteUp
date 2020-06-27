H, N = input().split()
H = int(H)
N = int(N)

skill = list(map(int, input().split()))
power = sorted(skill, reverse=True)

if sum(skill[:N]) >= H:
    print("Yes")
else:
    print("No")
