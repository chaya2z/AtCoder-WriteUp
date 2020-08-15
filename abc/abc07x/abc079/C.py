ABC_list = ["A", "B", "C"]

for i in range(1 << 3):
    print(bin(i)[2:].zfill(3))
