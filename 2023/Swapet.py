import sys

init_string = input().lower() # String de comparação
try_attempts = input() # Quantidade de testes

for _ in range(int(try_attempts)):
    word = input().lower() # Palavra a ser testada

    if sorted(word) != sorted(init_string):
        print("NAO", file=sys.stdout)
        continue

    diffs = [i for i in range(len(word)) if word[i] != init_string[i]]

    if len(diffs) == 0 or len(diffs) == 2:
        print("SIM", file=sys.stdout)
    else:
        print("NAO", file=sys.stdout)

    