def main():
    N, M, K = map(int, input().split())
    A_int_list = list(map(int, input().split()))
    B_int_list = list(map(int, input().split()))

    



if __name__ == '__main__':
    main()




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
