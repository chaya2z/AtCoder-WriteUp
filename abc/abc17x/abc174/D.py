N = int(input())
c_str = input()

r_num = c_str.count('R')
w_num = c_str.count('W')

true_list = 'R' * r_num + 'W' * w_num

if c_str == 'R' * N:
    print(0)
else:
    dif = 0
    for i in range(N):
        if c_str[i] != true_list[i]:
            dif += 1

    print(dif // 2)
