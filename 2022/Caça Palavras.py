import sys

n_words = int(input())
words = []
for _ in range(n_words):
    words.append(input())
n_lines = int(input())

word_hunt = []
word_lines = []
word_columns = []
for _ in range(n_lines):
    word_hunt.append(input().split(" "))
print(word_hunt, file=sys.stderr)

line = []
column = []
for l in word_hunt:
    for n in range(n_lines):
        line.append(l[n])
    word_lines.append("".join(line))
    line.clear()
print(word_lines, file=sys.stderr)
for n in range(n_lines):
    for c in word_hunt:
        column.append(c[n])
    word_columns.append("".join(column))
    column.clear()
print(word_columns, file=sys.stderr)

words_encountered = []
for l in word_lines:
    for n in range(len(words)):
        if words[n] in l:
            words_encountered.append(words[n])
for c in word_columns:
    for n in range(len(words)):
        if words[n] in c:
            words_encountered.append(words[n])

if len(words_encountered) == 0:
    print(0)
else:
    print(len(words_encountered))
    for c in words_encountered:
        print(c)
