S = input()
T = input()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == '@':
        if T[i] == 'a' or T[i] == 't' or T[i] == 'c' or T[i] == 'o' or T[i] == 'd' or T[i] == 'e' or T[i] == 'r':
            continue
        else:
            print("You will lose")
            exit()
    elif T[i] == '@':
        if S[i] == 'a' or S[i] == 't' or S[i] == 'c' or S[i] == 'o' or S[i] == 'd' or S[i] == 'e' or S[i] == 'r':
            continue
        else:
            print("You will lose")
            exit()
    else:
        print("You will lose")
        exit()

print("You can win")
