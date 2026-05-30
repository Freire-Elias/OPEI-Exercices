# Funções de lista Importantes

* map(int, input().split())  # lê vários valores na mesma linha
* max(lista, key=...)        # máximo com critério
* sorted(palavra)            # comparar anagramas
* sort(reversed=true)        # ordena em ordem decrescente
* Counter(palavra)           # contar letras rapidamente
* dict.get                   # Retorna valor da chave
* in lista                   # Está em lista
* lista.index(x)             # Posição do elemento x
* lista.count(x)             # Conta quantas vezes x aparece
* zip(lista1, lista2)        # Percorre as duas listas
* set([1, 2, 2, 3, 3, 3])    # Retira duplicatas
   

# Fatiamento

* lista[2:5]    # → [2, 3, 4]           (do índice 2 até 4)
* lista[:3]     # → [0, 1, 2]           (do início até 2)
* lista[3:]     # → [3, 4, 5]           (do índice 3 até o fim)
* lista[-1]     # → 5                   (último elemento)
* lista[-3:]    # → [3, 4, 5]           (últimos 3)
* lista[::-1]   # → [5, 4, 3, 2, 1, 0]  (invertida)