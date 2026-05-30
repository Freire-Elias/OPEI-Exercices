import sys
from itertools import groupby

"""
Dada uma string, comprima grupos de letras iguais consecutivas.
"""

string = input()
cstring = ""

for item, grupo in groupby(string):
    cstring += item + str(len(list(grupo)))

print(cstring)
