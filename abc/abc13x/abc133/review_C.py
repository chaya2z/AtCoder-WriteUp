# L, R = map(int, input().split())
#
# if R - L >= 2019:
#     print(0)
# elif L <= 3 and R >= 673:
#     print(0)
# else:
#     num_list = sorted(list(range(L, R + 1)))
#     print((num_list[0] * num_list[1]) % 2019)

L, R = map(int, input().split())
if (L <= 673 <= R and R - L >= 3) or (R - L >= 673):
    print(0)
else:
    mods = []
    mods_append = mods.append
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            m = (i * j) % 2019
            mods_append(m)
            if m == 2:
                break

    print(min(mods))
