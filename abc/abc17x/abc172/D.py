import math


# function to count the divisors
def count_divisors(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:

            # If divisors are equal,
            # count only one
            if n / i == i:
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2

    return cnt


def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * count_divisors(i)

    print(ans)


if __name__ == '__main__':
    main()
