bingo_int_list = [[int(i) for i in input().split()] for _ in range(3)]
N = int(input())
num_int_list = [int(input()) for _ in range(N)]
num_int_set = set(num_int_list)

bingo_bin_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        if bingo_int_list[i][j] in num_int_set:
            bingo_bin_list[i][j] = 1

# check row
for i in range(3):
    if sum(bingo_bin_list[i]) == 3:
        print('Yes')
        exit()

# check column
for i in range(3):
    if bingo_bin_list[0][i] + bingo_bin_list[1][i] + bingo_bin_list[2][i] == 3:
        print('Yes')
        exit()

# check diagonal
if bingo_bin_list[0][0] + bingo_bin_list[1][1] + bingo_bin_list[2][2] == 3 or bingo_bin_list[0][2] + bingo_bin_list[1][
    1] + bingo_bin_list[2][0] == 3:
    print('Yes')
    exit()

print('No')
