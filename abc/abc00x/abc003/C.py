N, K = map(int, input().split())
R = list(map(int, input().split()))
R = sorted(R)

now_rate = 0

for i in R[-K:]:
    now_rate += i
    now_rate /= 2

print(now_rate)
