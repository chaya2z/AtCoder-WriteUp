def main():
    N = int(input())
    table = [sorted(list(input())) for _ in range(N)]
    print(sorted(table))

    ans = 0
    cnt = 0

    for i in range(N):
        if table[i] == table[i + 1]:
            cnt += 1
        else:
            pass

    print(cnt)


if __name__ == '__main__':
    main()
