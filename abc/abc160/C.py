# AtCoder Beginner Contest 160

K, N = map(int, input().split())
A = list(map(int, input().split()))

ansdiv = K

# 一番近いやつ求める
for i, j in zip(A[:-1], A[1:]):
    div = K - j + i
    if div < ansdiv:
        ansdiv = div

# 最初のと最後のを忘れない
lastdiv = K - A[N-1] + A[0]
lastans = K - lastdiv
if lastans < ansdiv:
    ansdiv = lastans

print(ansdiv)
