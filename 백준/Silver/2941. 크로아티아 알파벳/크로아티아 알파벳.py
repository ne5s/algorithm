from sys import stdin

a = stdin.readline().rstrip()
print(len(a) - sum(a.count(s) for s in ['=', '-', 'lj', 'nj', 'dz=']))
