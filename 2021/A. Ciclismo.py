import sys

n_etapas = int(input())

for c in range(n_etapas):
    t, s, v = map(int, input().split())

    if v == 0:
        if s == 0:
            print("SIM")
        else:
            print("NAO")
        continue
    
    if t >= s / v:
        print("SIM")
    else:
        print("NAO")



    