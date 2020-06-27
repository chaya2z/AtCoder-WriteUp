# https://atcoder.jp/contests/abc153
#

H, A = input().split()
count = 0
H = int(H)
A = int(A)

while H > 0:
    H -= A
    count += 1

print(count)
