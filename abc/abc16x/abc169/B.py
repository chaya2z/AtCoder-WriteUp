# import functools
# import operator
#
# N = int(input())
# A_list = list(map(int, input().split()))
#
# prod = functools.partial(functools.reduce, operator.mul)
# ans = prod(A_list)
#
# if 10 ** 18 < ans:
#     print('-1')
# else:
#     print(ans)

# import numpy
#
# N = int(input())
# # A_list = list(map(int, input().split()))
# A_list = [10000] * 10000
# A_list = numpy.array(A_list)
# print(A_list)
# p = numpy.prod(A_list)
#
# if 1000000000000000000 < p:
#     print(-1)
# else:
#     print(p)


def main():
    N = int(input())
    A_list = list(map(int, input().split()))

    if 0 in set(A_list):
        print(0)
        exit()

    ans = 1
    for i in A_list:
        ans *= i
        if 1000000000000000000 < ans:
            print('-1')
            exit()
    else:
        print(ans)


main()
