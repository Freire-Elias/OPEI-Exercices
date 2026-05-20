import sys

n_acordes = int(input())
acordes = {}
lines = []
for _ in range(n_acordes):
    acorde = input()
    chave, valor = acorde.split(":")
    chave = chave.strip()
    valor = valor.strip()
    acordes[chave] = valor
print(acordes, file=sys.stderr)
for _ in range(6):
    lines.append(input())
print(lines, file=sys.stderr)

n = len(lines[0])
acordes_encontrados = {}

for c in range(2, n):
    test = []
    for n in range(6):
        test.append(lines[n][c])

    acorde = "".join(test)
    print(acorde, file=sys.stderr)

    for chave, valor in acordes.items():
        if acorde == valor:
            if chave not in acordes_encontrados:
                acordes_encontrados[chave] = 0
            acordes_encontrados[chave] += 1
if len(acordes_encontrados) == 0:
    print("Nenhum acorde foi encontrado na tablatura")
else:
    print("Acordes encontrados:")
    for chave, valor in acordes_encontrados.items():
        print(f"{valor}x acorde de {chave}")

