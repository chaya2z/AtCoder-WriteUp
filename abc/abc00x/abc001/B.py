m = int(input())

if m < 100:
    print("00")
elif m < 1000:
    print("0" + str(m)[0])
elif m <= 5000:
    print(m // 100)
elif 6000 <= m <= 30000:
    print(m // 1000 + 50)
elif 35000 <= m <= 70000:
    print(m // 5000 + 74)
else:
    print(89)
