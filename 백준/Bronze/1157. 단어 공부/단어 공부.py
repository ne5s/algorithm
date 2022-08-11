from sys import stdin

i=stdin.readline().rstrip().upper()
n=0
for p in map(chr,range(65,91)):
  q=i.count(p)
  if n<q:n,c=q,p
  elif n==q:c="?"
print(c)