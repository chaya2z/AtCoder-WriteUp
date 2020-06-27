import sys
input = sys.stdin.readline

def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    monster = list(map(int, input().split()))
    monster = sorted(monster, reverse=True)
    print(sum(monster[K:]))


if __name__ == "__main__":
    main()
