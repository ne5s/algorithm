from sys import stdin
S = stdin.readline().rstrip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(S.find(i), end = ' ')