A_x, A_y, B_x, B_y, C_x, C_y = map(int, input().split())

print(abs((A_x - C_x) * (B_y - C_y) - (B_x - C_x) * (A_y - C_y)) / 2)
