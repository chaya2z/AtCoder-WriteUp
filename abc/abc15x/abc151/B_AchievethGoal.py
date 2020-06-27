N, K, M = input().split()
test = list(map(int, input().split()))

sum_N_1 = sum(test)
if sum_N_1 / int(N) >= int(M):
    print(0)
elif (sum_N_1 + int(K)) / int(N) < int(M):
    print("-1")
else:
    print(int(M) * int(N) - sum_N_1)
