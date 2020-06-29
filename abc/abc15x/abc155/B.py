N = int(input())
A_int_list = list(map(int, input().split()))

for i in A_int_list:
    if i % 2 == 1:
        continue
    else:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            print('DENIED')
            exit()

print('APPROVED')
