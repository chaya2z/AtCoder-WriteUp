def main():
    N, K = map(int, input().split())
    comb_list = list(range(0, N + 1))
    rev_comb_list = reversed(comb_list[:-K])
    print(rev_comb_list)
    print(comb_list)
    ans = 0

    # ans += sum(comb_list[-K:]) - sum(comb_list[:K]) + 1
    start_min = sum(comb_list[:K])
    start_max = sum(comb_list[-K:])
    min_index = K - 1
    max_index = N - K + 1
    for i in range(N + 1):
        max_value = max_index - i
        min_value = min_index + i
        ans += max_value - min_value + 1

    print(ans)

    # for i in range(K, N + 1):
    #     ans += sum(comb_list[-i:]) - sum(comb_list[:i]) + 1
    #
    # print(ans + 1)


# N_factorial = math.factorial(N + 1)
#
# cnt = 0
#
# for i in range(K, N + 2):
#     cnt += N_factorial // (math.factorial(i) * math.factorial(N + 1 - i))
#
# print(cnt)

if __name__ == '__main__':
    main()
