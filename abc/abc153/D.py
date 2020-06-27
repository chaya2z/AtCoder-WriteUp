import sys
import math

input = sys.stdin.readline

def main():
    H = int(input())
    print(2 ** int((math.log(H, 2)) + 1) - 1)


if __name__ == "__main__":
    main()
