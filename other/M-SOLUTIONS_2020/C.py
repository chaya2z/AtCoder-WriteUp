def main():
    N, K = map(int, input().split())
    A_int_list = list(map(int, input().split()))

    l_int = A_int_list[0]

    for i in range(1, N):
        if l_int < A_int_list[K + i - 1]:
            print("Yes")
        else:
            print("No")

        if K + i == N:
            exit()
        l_int = A_int_list[i]


if __name__ == '__main__':
    main()
