def powo(x, y):
    if y == 0:
        return x
    return x * powo(x, y-1)

def counter(x):
    if x // 10 <= 0:
        return 1
    return 1 + counter(x // 10)

def palindromo(str):
    if len(str) <= 1:
        return "SIM"
    if str[0] == str[-1]:
        return palindromo(str[1:-1])
    else:
        return "NAO"

def sum(num):
    if len(num) <= 1:
        return num[0]
    return num[0] + sum(num[1:])
