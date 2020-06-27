# 入力
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A_i, B_i までの合計
a, b = [0], [0]
for i in range(N):
    a.append(a[i] + A[i])
for i in range(M):
    b.append(b[i] + B[i])

# B_j < K - A_i
#
# for
# A_1, A_2...A_N というように増えていく
ans, j = 0, M
for i in range(N + 1):
    # Aの合計がKを超えたらBが入り込む余地はない
    if a[i] > K:
        break
    # A_i のときのBの最大個数を求める
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i + j)
# 全部のパターンを試したあと最大の個数が求まっている
print(ans)


# def main():
#     N, M, K = map(int, input().split())
#     A_int_list = list(map(int, input().split()))
#     B_int_list = list(map(int, input().split()))
#
#     min_sum = 0
#
#     for i in range(N + M):
#         if len(A_int_list) != 0 and len(B_int_list) != 0:
#             if A_int_list[0] < B_int_list[0]:
#                 min_sum += A_int_list[0]
#                 A_int_list.pop(0)
#             else:
#                 min_sum += B_int_list[0]
#                 B_int_list.pop(0)
#
#         elif len(A_int_list) == 0:
#             min_sum += B_int_list[0]
#             B_int_list.pop(0)
#
#         elif len(B_int_list) == 0:
#             min_sum += A_int_list[0]
#             A_int_list.pop(0)
#
#         if K < min_sum:
#             print(i)
#             exit()
#
#     print(N + M)
#     exit()
#
#
# if __name__ == '__main__':
#     main()
