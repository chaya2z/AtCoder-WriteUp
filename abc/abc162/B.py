N = int(input())
total = sum(range(N + 1))

fizz_total = sum(range(0, N + 1, 3))
buzz_total = sum(range(0, N + 1, 5))
fizzbuzz_total = sum(range(0, N + 1, 15))

print(total - fizz_total - buzz_total + fizzbuzz_total)
