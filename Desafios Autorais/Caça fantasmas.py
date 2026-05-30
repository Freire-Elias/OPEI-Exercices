import sys

"""
Num tabuleiro NxN, fantasmas são representados por 'F' e armadilhas por 'A'. Um caça-fantasmas começa numa posição e se move seguindo instruções (N, S, L, O). Se cair numa armadilha para. Se pegar um fantasma soma 10 pontos. Imprima a pontuação final e a posição.
"""

tabuleiro = int(input())
matriz = []
for l in range(tabuleiro):
    matriz.append(input().split())

print(matriz, file=sys.stderr)

directions = input()

x = y = points = 0
caiu = False
for d in directions:
    match d:
        case "N":
            y += 1
        case "S":
            y -= 1
        case "R":
            x += 1
        case "L":
            x -= 1
    if y > tabuleiro or x > tabuleiro or caiu:
        break
    print(matriz[y][x], file=sys.stderr)
    if matriz[y][x] == "F":
        points += 10
    if matriz[y][x] == "A":
        caiu = True
        break

if y > tabuleiro or x > tabuleiro or caiu:
    print(f"PERDEU NA POSIÇÃO {x},{y}")
else:
    print(f"Pontos: {points}")
    print(f"Posição final: {x}, {y}")
