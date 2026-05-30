# Operadores importantes em listas

* Todos satisfazem condição all(x > 0 for x in lista)
* Algum satisfaz condição any(x > 0 for x in lista)

**a = {1, 2, 3, 4}**
**b = {3, 4, 5, 6}**

* a | b   # união               → {1, 2, 3, 4, 5, 6}
* a & b   # interseção          → {3, 4}
* a - b   # diferença           → {1, 2}  (está em a mas não em b)
* a ^ b   # diferença simétrica → {1, 2, 5, 6} (está em um mas não nos dois)