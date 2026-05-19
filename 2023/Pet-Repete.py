import sys

abc = ["a", "b", "c", "d", "e", "f",
"g", "h", "i", "j", "k", "l",
"m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x", "y", "z"]

n = int(input())

tables = []
for c in range(n):
    tables.append(input().split())
print(tables, file=sys.stderr)

nmax = 0
for i in abc:
    for t in tables:
        n1 = t[0].count(i)
        n2 = t[1].count(i)
        if n1 >= n2:
            nmax += n1
        else:
            nmax += n2
    print(nmax)
    nmax = 0
