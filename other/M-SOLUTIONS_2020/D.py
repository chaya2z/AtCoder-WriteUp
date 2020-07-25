N = int(input())
A_int_list = list(map(int, input().split()))

money = 1000
stock = 0

for i in range(N - 1):
    if A_int_list[i] < A_int_list[i + 1]:
        stock = money // A_int_list[i]
        money = money % A_int_list[i]
        money += stock * A_int_list[i + 1]
        stock = 0

print(money)
