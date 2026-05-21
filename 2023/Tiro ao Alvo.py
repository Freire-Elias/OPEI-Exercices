import sys

matriz = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

n_players = int(input())
players = {}
for _ in range(n_players):
    name = input()
    acertos = []
    pontos = 0
    for c in range(10):
        acertos.append(input())
    print(acertos, file=sys.stderr)
    for c in range(10):
        for i, n in enumerate(matriz[c]):
            print(i, n, file=sys.stderr)
            if acertos[c][i] == "X":
                pontos += n
    print(f"{name}: {pontos}")
    players[name] = pontos

winner = max(players, key=players.get)
print(f"{winner} venceu fazendo {players[winner]} pontos")

