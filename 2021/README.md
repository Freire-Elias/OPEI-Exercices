# Bibliotecas Uteis

**itertools groupby**

* Conta items consecutivos
* f = 1122113
'''for item, grupo in groupby(f)'''
'''    print(item, len(list(grupo)))'''

**itertools permutation**

* faz permutação entre itens
permutation([1, 2 , 3]) 3 2 1 / 2 1 3 / 3 1 2...

**itertools combination**

* faz combinação entre itens
combination([1, 2 ,3], 2) [(1, 2), (1, 3)]
