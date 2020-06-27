# AtCoder Beginner Contest 160

X = int(input())


a = X // 500
b = X % 500
ans = a * 1000

b = b // 5
ans = ans + b*5

print(ans)
