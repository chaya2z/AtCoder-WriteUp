# import math
# from functools import reduce
#
#
# def gcd(*numbers):
#     return reduce(math.gcd, numbers)
#
#
# def gcd_list(numbers):
#     return reduce(math.gcd, numbers)
#
#
# def main():
#     K = int(input())
#
#     test = [gcd(i, j, k) for i in range(1, K + 1) for j in range(1, K + 1) for k in range(1, K + 1)]
#     print(sum(test))
#
#
# if __name__ == '__main__':
#     main()

K = int(input())
ans = 0
total_comb = K ** 2
cnt = 0

for i in range(1, K + 1):
    comb = (K // i) ** 2
    ans += comb * i
    ans += K ** 2 - comb


print(ans)

