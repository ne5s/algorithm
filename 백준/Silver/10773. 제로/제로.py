from sys import stdin

n = int(stdin.readline())
stack = []
for i in range(n):
    a = int(stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))
