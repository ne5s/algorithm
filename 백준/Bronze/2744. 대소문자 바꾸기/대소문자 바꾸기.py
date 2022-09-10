from sys import stdin

a = stdin.readline().rstrip()
b = ''
for i in a:
    if ord(i) >= 65 and ord(i) <= 90:
        b += chr(ord(i)+32)
    elif ord(i) >= 97 and ord(i) <= 122:
        b += chr(ord(i) - 32)
print(b)