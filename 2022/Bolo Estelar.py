import sys

n_camadas = int(input())

if n_camadas == 1 or n_camadas == 2:
    print(1)
else:
    sequence = [1, 1, 2]
    for c in range(n_camadas - 3):
        sequence.append((sequence[-1] + sequence[-2]))
    print(sequence[-1])
        