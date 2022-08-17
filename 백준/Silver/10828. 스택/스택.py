from sys import stdin

n = int(stdin.readline())
stack = []
for i in range(n):
    temp = stdin.readline()
    cmd = temp.split()[0]
    if cmd == 'push':
        stack.append(temp.split()[1])
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]

    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif cmd == 'top':
        print(-1) if len(stack) == 0 else print(stack[-1])
