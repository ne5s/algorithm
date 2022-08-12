from sys import stdin

a = stdin.readline().rstrip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro:
    if i in a:
        a = a.replace(i, '1')
print(len(a))
