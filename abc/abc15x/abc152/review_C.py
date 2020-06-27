#
# ABC152 2020/1/19
#
# https://atcoder.jp/contests/abc152/tasks/abc152_c
#

# import sys
#
# input = sys.stdin.readline
#
#
# def main():
#     N = int(input())
#     P = list(map(int, input().split()))
#
#     cnt = 1
#     min_num = P[0]
#     for p in P:
#         if p < min_num:
#             min_num = p
#             cnt += 1
#
#     print(cnt)
#
#
# if __name__ == "__main__":
#     main()


# def main():
#     inf = float("inf")
#
#     n = int(input())
#     *p, = map(int, input().split())
#
#     ma = inf
#     ret = 0
#     for x in p:
#         if x <= ma:
#             ret += 1
#             ma = x
#     print(ret)
#
# if __name__ == "__main__":
#     main()

