import numpy as np

N = int(input())

alphabet_dict = {'0': 'a', '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
                 'A': 'j',
                 'B': 'k',
                 'C': 'l', 'D': 'm', 'E': 'n', 'F': 'o', 'G': 'p', 'H': 'q', 'I': 'r', 'J': 's', 'K': 't',
                 'L': 'u',
                 'M': 'v', 'N': 'w', '': 'x', 'O': 'y', 'P': 'z'}
ans = []

n_list_base26 = list(np.base_repr(N, base=26))

for i in n_list_base26:
    ans.append(alphabet_dict[i])


ans = ''.join(ans)
print(ans)
