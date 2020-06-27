def main():
    N, M, *a = map(int, open(0).read().split())
    div = 1000000007
    broken = set(a)

    comb_list = [0] * (N + 1)
    comb_list[0] = 1
    if 1 not in broken:
        comb_list[1] = 1

    for i in range(2, N + 1):
        if i in broken:
            continue
        comb_list[i] = (comb_list[i - 1] + comb_list[i - 2]) % div

    print(comb_list[-1])


if __name__ == "__main__":
    main()
