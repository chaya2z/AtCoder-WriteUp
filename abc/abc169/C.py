# import math
#
# A, B = input().split()
# A = int(A)
# B = list(B)
#
# tmp1 = A * int(B[0])
# tmp2 = A * int(B[2])
# tmp3 = A * int(B[3])
#
# tmp4 = str(tmp2)[:-1]
# tmp4 = int(tmp4)
# tmp5 = str(tmp3)[:-2]
# tmp5 = int(tmp5)
#
# tmp6 = str(tmp2)[-1:]
# tmp7 = str(tmp3)[-2:]
# tmp8 = int(tmp6) + int(tmp7)
# tmp8 = str(tmp8)[:-2]
# tmp8 = int(tmp8)
#
# print(tmp1 + tmp4 + tmp5 + tmp8)

A, B = input().split()
A = int(A)
B = list(B)

tmp1 = A * int(B[0])
tmp2 = A * int(B[2])
tmp3 = A * int(B[3])

tmp2 /= 10
tmp3 /= 100

ans = tmp1 + tmp2 + tmp3
ans = str(ans)
print(ans.split('.')[0])
