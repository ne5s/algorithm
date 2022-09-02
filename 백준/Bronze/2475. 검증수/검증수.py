from sys import stdin
li = list(map(int, stdin.readline().split()))
sum = 0
for i in li:
    sum += (i**2)

print(sum % 10)