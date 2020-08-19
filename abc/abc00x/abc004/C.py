def main():
    N = int(input())
    N %= 30

    card = [1, 2, 3, 4, 5, 6]

    for i in range(N):
        mod = i % 5
        card[mod], card[mod + 1] = card[mod + 1], card[mod]

    card = map(str, card)
    print(''.join(card))


if __name__ == '__main__':
    main()
