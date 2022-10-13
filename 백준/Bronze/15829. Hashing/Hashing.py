from sys import stdin

L = int(stdin.readline())
a = stdin.readline().rstrip()
suma = 0
for i in range(L):
    suma = suma + (ord(a[i])-96) * (31 ** i)
print(suma % 1234567891)