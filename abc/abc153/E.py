import sys
input = sys.stdin.readline

def main():
    H, N = input().split()
    H = int(H)
    N = int(N)
    magic = [list(map(int, input().split())) for _ in range(N)]
    cost = [[round(magic[i][0] / magic[i][1], 1), magic[i]] for i in range(N)]
    cost = sorted(cost, reverse=True)
    cost2 = [int(i) for i in cost if int(cost[i][0]) == int(cost[0][0])]
    print(cost2)

if __name__ == "__main__":
    main()
