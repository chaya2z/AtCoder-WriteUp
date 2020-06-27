import math

N, K = map(int, input().split())
mod = 10 ** 9 + 7

red_num = N - K
red_num_fact = math.factorial(red_num)

cnt = 0

for i in range(1, K + 1):
    ans = math.factorial(red_num + i) // (red_num_fact * math.factorial(i))
    print(ans % mod)
