import sys

"""
Dado N, gere uma matriz NxN preenchida em espiral.
"""

n = int(input())
matriz = [[0] * n for _ in range(n)]
nx = 1
top = 0
down = n-1
right = n-1
left = 0
while top <= down and left <= right:
    for c in range(left, right+1):
        matriz[top][c] = nx
        nx += 1
    top += 1
    for c in range(top, down+1):
        matriz[c][right] = nx
        nx += 1
    right -= 1
    for c in range(right, left-1, -1):
        matriz[down][c] = nx
        nx += 1
    down -= 1
    for c in range(down, top-1, -1):
        matriz[c][left] = nx
        nx += 1
    left += 1

for c in range(n):
    for l in range(n):
        print(matriz[c][l], end=" ")
    print()