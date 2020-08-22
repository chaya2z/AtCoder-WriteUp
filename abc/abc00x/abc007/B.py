A = input()

if A == "a":
    print(-1)
elif len(A) == 1:
    code = ord(A)
    print(chr(code - 1))
else:
    print(A[:-1])
