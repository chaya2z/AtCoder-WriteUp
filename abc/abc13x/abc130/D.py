def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    ans_list = [N - i + 1 for j in range(N) for i in range(1, N + 1) if K <= sum(a[j:i])]
    # for j in range(N):
    #     for i in range(1, N + 1):
    #         sum_a = sum(a[j:i])
    #         if K <= sum_a:
    #             ans += N - i + 1
    #             break
    print(sum(ans_list))


if __name__ == "__main__":
    main()
