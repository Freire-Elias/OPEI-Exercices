import sys

word = input()
print(word[::-1])
print(len(word), file=sys.stderr)
print(len(word) % 2, file=sys.stderr)
if len(word) % 2 == 0:
    print("E um Patrimonio Imaterial")
else:
    print("Nao e um Patrimonio Imaterial")