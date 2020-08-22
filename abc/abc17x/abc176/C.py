def main():
    N = int(input())
    A = list(map(int, input().split()))

    h = A[0]
    ans = 0

    for i in A:
        if i < h:
            ans += h - i
        elif h < i:
            h = i

    print(ans)


if __name__ == '__main__':
    main()
