import sys

testes = int(input())

for _ in range(testes):
    valores = input().split()
    valores_int = list(map(int, valores))
    n_malas = valores_int[0]
    n_janela = valores_int[1]

    malas = []
    for c in range(n_malas):
        malas.append(int(input()))
        print(malas, file=sys.stderr)
        print(malas[:-n_janela], file=sys.stderr)
        print(malas[1: 1 + n_janela], file=sys.stderr)
    
    max_list = 0
    for i, c in enumerate(malas[:-n_janela + 1]):
        print(malas[i:i + n_janela], file=sys.stderr)
        n = sum(malas[i:i + n_janela])
        if n > max_list:
            max_list = n

    
    print(f"A maior soma de peso s é {max_list}")
    
