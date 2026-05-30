import sys
from itertools import groupby

n = int(input())
f = "1"

for _ in range(n-1):
    next = ""
    for n, g in groupby(f):
        next += str(len(list(g))) + n
    f = next
print(f)