import sys


n_players = int(input())
players = {}

for c in range(n_players):
    nome, v, d = input().split()
    players[nome] = (int(v), int(d))

for nome, partidas in players.items():
    vic_per = (partidas[0] / sum(partidas)) * 100
    print(f"{nome} {vic_per}%")
