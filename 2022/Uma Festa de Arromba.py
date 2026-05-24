import sys

n_columns = int(input())
n_lines = int(input())
matriz = []
line = []
for c in range(n_columns):
    n = input().split(" ")
    matriz.append(list(map(int, n)))
print(matriz, file=sys.stderr)

if n_columns != n_lines:
    print("Infelizmente não ouviremos a linda voz de César este ano...")
else:
    custo = 0
    iterator = 0
    for m in range(len(matriz)):
        custo += (matriz[m][iterator])
        iterator += 1
    matriz.reverse()
    iterator = 0
    for m in range(len(matriz)):
        custo += (matriz[m][iterator])
        iterator += 1
  
    print(f"Este terreno está ótimo para o evento, e custa apenas R${custo:.2f}!")

