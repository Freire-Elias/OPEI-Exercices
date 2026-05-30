import sys
import string

"""
Dado um texto e uma chave K, cifre o texto deslocando cada letra K posições no alfabeto 
"""

alfabeto = list(string.ascii_uppercase)
word = input().upper()
n = int(input())
cifra = ""

for c in word:
    x = alfabeto.index(c)
    cifra += alfabeto[x+n]

print(cifra)