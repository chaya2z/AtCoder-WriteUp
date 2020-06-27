a, b = input().split()

word_a = a * int(b)
word_b = b * int(a)

word_list = [word_a, word_b]
word_list.sort()
print(word_list[0])
