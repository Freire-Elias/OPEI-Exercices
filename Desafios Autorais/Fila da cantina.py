import sys

"""
Os alunos estão na fila da cantina. Dado o nome e o tempo de atendimento de cada aluno, calcule o tempo de espera de cada um.
"""

n_alunos = int(input())
alunos = {}

for c in range(n_alunos):
    nome, tempo = input().split()
    alunos[nome] = int(tempo)

time = 0

for nome, tempo in alunos.items():
    print(f"{nome} esperou {time} minutos")
    time += tempo

