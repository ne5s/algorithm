from sys import stdin

sik = stdin.readline().rstrip()

b = sik.split('-')
result = 0
for i in range(len(b)):
    c = list(map(int, b[i].split('+')))
    if i == 0:
        result += sum(c)
    else:
        result -= sum(c)
print(result)